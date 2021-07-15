#!/usr/bin/env python
# coding: utf-8

# In[1]:


H,W = list(map(int, input().split()))
c = []
for _ in range(10):
    c.append(list(map(int, input().split())))
A = []
for _ in range(H):
    A.append(list(map(int, input().split())))


# In[3]:


def wf_func(mat):
    dist = mat
    for k in range(10):
        for i in range(10):
            for j in range(10):
                dist[i][j] = min(dist[i][j], dist[i][k]+dist[k][j])
    return dist


# In[5]:


dist = wf_func(c)
ans = 0
for i in range(H):
    for j in range(W):
        if A[i][j] != -1:
            ans += dist[A[i][j]][1]
print(ans)


# In[ ]:





