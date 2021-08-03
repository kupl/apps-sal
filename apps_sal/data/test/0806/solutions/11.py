#!/usr/bin/env python
# coding: utf-8

# In[22]:


stuff = list(map(int, input().rstrip().split()))


# In[23]:


n = stuff[0]
l = stuff[1]
r = stuff[2]

mod = 10**9 + 7


# In[24]:


zeromods = r // 3 - (l - 1) // 3

onemods = (r - 1) // 3 - (l - 2) // 3

twomods = (r - 2) // 3 - (l - 3) // 3


# In[25]:


combos = [[0, 0, 0] for i in range(n)]


# In[26]:


combos[0] = [zeromods, onemods, twomods]


# In[28]:


for i in range(1, n):
    combos[i][0] = (combos[i - 1][0] * zeromods + combos[i - 1][1] * twomods + combos[i - 1][2] * onemods) % mod

    combos[i][1] = (combos[i - 1][0] * onemods + combos[i - 1][1] * zeromods + combos[i - 1][2] * twomods) % mod

    combos[i][2] = (combos[i - 1][0] * twomods + combos[i - 1][1] * onemods + combos[i - 1][2] * zeromods) % mod


print(combos[-1][0])


# In[29]:


combos


# In[ ]:
