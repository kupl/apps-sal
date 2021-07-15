#!/usr/bin/env python
# coding: utf-8

# In[15]:


import math
ns=list(map(int, input().rstrip().split()))
n=ns[0]
s=ns[1]

data=list(map(int, input().rstrip().split()))


# In[16]:


data.sort()


# In[17]:


extras=[i-data[0] for i in data]


# In[18]:


total=sum(data)
extratotal=sum(extras)


# In[ ]:





# In[19]:


if s>total:
    print(-1)
elif extratotal>=s:
    print(data[0])    
else:
    sub=math.ceil((s-extratotal)/n)
    print(data[0]-sub)
    


# In[ ]:


