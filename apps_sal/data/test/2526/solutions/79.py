#!/usr/bin/env python
# coding: utf-8

# In[10]:


X, Y, A, B, C = list(map(int, input().split()))
p = sorted(list(map(int, input().split())), reverse=True)
q = sorted(list(map(int, input().split())), reverse=True)
r = sorted(list(map(int, input().split())), reverse=True)


# In[14]:


p_list = p[:X]
q_list = q[:Y]
mylist = sorted(p_list + q_list + r, reverse=True)
ans = 0
for i in range(X + Y):
    ans += mylist[i]
print(ans)


# In[ ]:
