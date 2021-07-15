#!/usr/bin/env python
# coding: utf-8

# In[38]:


string=list(input())


# In[39]:


n=len(string)


# In[11]:





# In[40]:


asubsets=[]
a=0
b=1
for i in range(n):

        if string[i]=="a":
            a=a+1
            
            
        if string[i]=="b":
            asubsets.append(a)
            a=0
            
asubsets.append(a)    
#print(asubsets)


# In[41]:


increase=[i+1 for i in asubsets]


# In[42]:


total=1

for i in increase:
    total=total*i
    


# In[43]:


finaltotal=(total-1)%(pow(10,9)+7)


# In[44]:


print(finaltotal)


# In[ ]:

