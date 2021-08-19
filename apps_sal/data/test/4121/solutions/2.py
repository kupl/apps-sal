#!/usr/bin/env python
# coding: utf-8

# In[4]:


import math
n = int(input())
columns = list(map(int, input().rstrip().split()))


# In[5]:


modcolumns = [i % 2 for i in columns]


# In[6]:


test = 0


# In[7]:


previouslist = []


for i in range(0, n):
    if len(previouslist) == 0:
        previouslist.append(modcolumns[i])

    elif modcolumns[i] == previouslist[-1]:
        previouslist.pop()

    else:
        previouslist.append(modcolumns[i])


if len(previouslist) <= 1:
    print("YES")
else:
    print("NO")


# In[ ]:
