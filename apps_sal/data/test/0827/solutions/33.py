#!/usr/bin/env python
# coding: utf-8

# In[1]:


N = int(input())
T = input()


# In[2]:


l = 10**10
s = '110' * ((10**5) + 1)
ans = 0
if T == '1':
    ans = l * 2
else:
    for i in range(3):
        if s[i:N + i] == T:
            ans = l - ((i + N - 1) // 3)
            break
print(ans)


# In[ ]:
