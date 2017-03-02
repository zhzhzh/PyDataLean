# IPython log file

import numpy as np
from numpy.random import randn
data = {i: randn() for i in range(7)}
data
an_apple = 27
an_example = 42
b = [1,2,3]
import datetime
get_ipython().magic('pinfo b')
get_ipython().magic('quickref')
def add_numbers(a, b):
    """
    Add two numbers together
    
    Returns
    -------
    the_sum : type of arguments
    """
    return a + b
get_ipython().magic('pinfo add_numbers')
get_ipython().magic('pinfo2 add_numbers')
get_ipython().magic('psearch np.*load*')
get_ipython().magic('run ipython_script_test.py')
c
result
get_ipython().magic('run pydata-book/ch03/ipython_bug.py')
a = np.random.randn(100, 100)
get_ipython().magic('timeit np.dot(a, a)')
get_ipython().magic('time np.dot(a, a)')
get_ipython().magic('who')
get_ipython().magic('who_ls')
get_ipython().magic('whos')
get_ipython().magic('xdel a')
get_ipython().magic('whos')
get_ipython().magic('logstart')
get_ipython().magic('whos')
get_ipython().system('python')
