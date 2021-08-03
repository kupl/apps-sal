#!/usr/bin/env python
# coding: utf-8

# In[26]:


N, K = list(map(int, input().split()))
x = list(map(int, input().split()))


# In[35]:


ans = 10**10
for i in range(N - K + 1):
    ans = min(ans, abs(x[i]) + (x[i + K - 1] - x[i]), abs(x[i + K - 1]) + (x[i + K - 1] - x[i]))
print(ans)


# In[ ]:
