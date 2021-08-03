#!/usr/bin/env python
# coding: utf-8

# In[1]:


N = int(input())
A = list(map(int, input().split()))


# In[18]:


mod = 10**9 + 7
ans = 0
for n in range(61):
    ones = sum([1 for a in A if (a >> n) & 1])
    ans += (1 << n) * ones * (N - ones)
    ans %= mod

print(ans)


# In[ ]:
