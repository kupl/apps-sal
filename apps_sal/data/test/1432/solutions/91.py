#!/usr/bin/env python
# coding: utf-8

# In[18]:


N = int(input())
A = list(map(int, input().split()))


# In[19]:


s = sum(A)
x = s - sum(A[1::2])*2
ans = [x]
for i in range(N-1):
    x = 2*A[i]-x
    ans += [x]
print((*ans))


# In[ ]:





