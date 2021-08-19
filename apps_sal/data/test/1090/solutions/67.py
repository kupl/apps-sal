#!/usr/bin/env python
# coding: utf-8

# In[1]:


N, K = list(map(int, input().split()))
S = input()


# In[2]:


cnt = 1
for i in range(N - 1):
    if S[i] != S[i + 1]:
        cnt += 1
cnt = max(1, cnt - K * 2)
print((N - cnt))


# In[ ]:
