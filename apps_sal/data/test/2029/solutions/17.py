#!/usr/bin/env python
# coding: utf-8

# In[ ]:


n, s=list(map(int, input().split()))


# In[ ]:


edgecount=[0 for i in range(n)]


# In[ ]:


for j in range(0,n-1):
    e1, e2=list(map(int, input().split()))
    edgecount[e1-1]+=1
    edgecount[e2-1]+=1
    
    
nodecount=0

for i in range(0,n):
    if edgecount[i]==1:
        nodecount+=1

print(s*2/nodecount)
    


