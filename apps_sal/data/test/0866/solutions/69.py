#!/usr/bin/env python
# coding: utf-8

# In[8]:


def nCk(n, k, mod):
    a = 1
    for i in range(n, n-k, -1):
        a *= i
        a %= mod
    b = 1
    for i in range(1, k+1):
        b *= i
        b %= mod
    a *= pow(b, mod-2, mod)
    return a


# In[12]:


x,y = list(map(int,input().split()))


# In[14]:


mod = 10**9+7
if (x+y)%3 != 0:
    ans = 0
else:
    right = x - (x+y)//3
    up = y - (x+y)//3
    if right < 0 or up < 0:
        ans = 0
    else:
        ans = nCk(right+up,right,mod)%mod
print(ans)


# In[ ]:





