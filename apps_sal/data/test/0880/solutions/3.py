#!/usr/bin/env python
# coding: utf-8

# In[35]:

#import time

n=int(input())


# In[36]:


# In[37]:


fac=1
#t1 = time.time()

for i in range(2,n+1):
    fac=fac*i%998244353

#t2 = time.time()


total=(n-1)*fac%998244353
dsum=0
diff=1
for i in range(0,n-2):
    
    diff=diff*(n-i)%998244353
    #print(diff)    
    dsum+=diff%998244353    

answer=(total-dsum)%998244353
# In[38]:

#t3 = time.time()

#print(t3-t2,t2-t1)

if n==1:
    print(1)
else:    
    print(answer)


# In[31]:

