#!/usr/bin/env python
# coding: utf-8

# In[8]:


import sys
sys.setrecursionlimit(10**9)


# In[10]:


n = int(input())
ab = []
t = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = [int(x) - 1 for x in input().split()]
    t[a].append(b)
    t[b].append(a)
    ab.append((min(a, b), max(a, b)))


# In[11]:


k = max(list(map(len, t)))
d = {}


def dfs(pre, cur, col):
    cn = 1 if col != 1 else 2
    for i in t[cur]:
        if i == pre:
            continue
        d[(min(i, cur), max(i, cur))] = cn
        dfs(cur, i, cn)
        cn += 1
        if col == cn:
            cn += 1


dfs(0, 0, 0)
print(k)
for i in ab:
    print((d[i]))


# In[ ]:
