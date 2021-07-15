#!/usr/bin/env python
# coding: utf-8

# In[14]:


import math
n=int(input())
blist=list(map(int, input().rstrip().split()))


# In[15]:


alist=[0 for i in range(n)]


# In[16]:


alist[0]=0
alist[n-1]=blist[0]

for i in range(1,n//2):
    if blist[i]<=blist[i-1]:
        alist[i]=alist[i-1]
        alist[n-i-1]=blist[i]-alist[i]
    else:
        alist[n-i-1]=alist[n-i]
        alist[i]=blist[i]-alist[n-i-1]
        


# In[17]:


aliststr=[str(i) for i in alist]

print(" ".join(aliststr))


# In[ ]:


