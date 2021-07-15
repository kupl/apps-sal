#!/usr/bin/env python
# coding: utf-8

# In[13]:


import math


# In[11]:


N,H = list(map(int, input().split()))
a_list = [];b_list = []
for _ in range(N):
    a,b = list(map(int,input().split()))
    a_list.append(a)
    b_list.append(b)


# In[14]:


a_max = max(a_list)
b_list = sorted(b_list,reverse=True)
b_list.append(0)
h = H
ans = 0
for b in b_list:
    if b >= a_max:
        ans += 1
        h -= b
        if h <= 0:
            break
    else:
        ans += math.ceil(h/a_max)
        break
print(ans)


# In[ ]:





