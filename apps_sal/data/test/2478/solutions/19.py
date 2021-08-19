#!/usr/bin/env python
# coding: utf-8

# In[1]:


N = int(input())
S = input()


# In[2]:


l = 0
r = 0
for s in S:
    if s == "(":
        r += 1
    else:
        if r > 0:
            r -= 1
        else:
            l += 1
ans = "".join(["(" * l, S, ")" * r])
print(ans)


# In[ ]:
