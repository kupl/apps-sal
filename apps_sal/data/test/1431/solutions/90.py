#!/usr/bin/env python
# coding: utf-8

# In[3]:


N = int(input())
a = list(map(int, input().split()))


# In[6]:


mylist = [0] * (N + 1)
i = N
while i > 0:
    idx = i
    x = 0
    while idx <= N:
        x += mylist[idx]
        idx += i
    if x % 2 != a[i - 1]:
        mylist[i] = 1
    i -= 1
ans = []
for i in range(1, N + 1):
    if mylist[i] == 1:
        ans.append(i)
print((len(ans)))
if ans:
    print((*ans))


# In[ ]:
