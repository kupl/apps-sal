#!/usr/bin/env python
# coding: utf-8

# In[3]:


from itertools import product


# In[16]:


S = input()


# In[17]:


length = len(S)
ans = 0
for lst in product(["+",""], repeat=length-1):
    mystr = ""
    for i in range(length-1):
        mystr += S[i]+lst[i]
    mystr += S[-1]
    mylist = [int(x) for x in mystr.split("+")]
    ans += sum(mylist)
print(ans)


# In[ ]:





