#!/usr/bin/env python
# coding: utf-8

# In[1]:


n, a, b = list(map(int, input().split()))


# In[2]:


def nCk(n, k, mod):
    a = 1
    for i in range(n, n - k, -1):
        a *= i
        a %= mod
    b = 1
    for i in range(1, k + 1):
        b *= i
        b %= mod
    a *= pow(b, mod - 2, mod)
    return a


# In[3]:


mod = 10**9 + 7
ans = pow(2, n, mod) - 1
ans -= nCk(n, a, mod) + nCk(n, b, mod)
print((ans % mod))


# In[ ]:
