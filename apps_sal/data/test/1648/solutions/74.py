#!/usr/bin/env python
# coding: utf-8

# In[1]:


N,K = list(map(int, input().split()))


# In[5]:


mod = 10**9+7
def nCr(N, R, mod):
    R = min(R, N-R)
    numer = denom = 1
    for i in range(1, R+1):
        numer = numer * (N+1-i) % mod
        denom = denom * i % mod
    res = numer * pow(denom, mod-2, mod) % mod
    return res


# In[7]:


for i in range(1,K+1):
    if N-K+1<i:
        print((0))
        continue
    y = nCr(N-K+1,i,mod)
    y *= nCr(K-1,i-1,mod)
    print((y%mod))


# In[ ]:





