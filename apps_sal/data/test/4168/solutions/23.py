#!/usr/bin/env python
# coding: utf-8

# In[6]:


N = int(input())


# In[7]:


a = ""
if N == 0:
    a = 0
while N != 0:
    if N % 2 != 0:
        N -= 1
        a = "1" + a
    else:
        a = "0" + a
    N //= -2
print(a)


# In[ ]:
