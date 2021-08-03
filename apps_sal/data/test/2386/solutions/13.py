#!/usr/bin/env python
# coding: utf-8

# In[32]:


import numpy as np


# In[22]:


N = int(input())
A = list(map(int, input().split()))


# In[41]:


a = np.array(A)
b = a - np.arange(1, N + 1)
c = np.median(b)
d = abs(b - c).sum()
print((int(d)))


# In[ ]:
