#!/usr/bin/env python
# coding: utf-8

# In[1]:


N = int(input())
xyh = []
for _ in range(N):
    xyh.append(list(map(int, input().split())))


# In[4]:


xyh.sort(key=lambda x:x[2],reverse=True)
ans = []
for cx in range(101):
    for cy in range(101):
        x,y,h = xyh[0]
        ch = h + abs(x-cx) + abs(y-cy)
        if all([h == max(ch-abs(x-cx)-abs(y-cy),0) for x,y,h in xyh[1:]]):
            ans = [cx,cy,ch]
            break
    else:
        continue
    break
print((*ans))


# In[ ]:





