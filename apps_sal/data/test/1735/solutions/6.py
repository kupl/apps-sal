#!/usr/bin/env python
# coding: utf-8

# In[19]:


word=list(input())


# In[20]:


n=len(word)


# In[21]:


emptyword=[]


# In[22]:


popcount=0


# In[23]:


for i in range(n):
    if len(emptyword)==0:
        emptyword=[word[i]]
    else:
        if word[i]==emptyword[-1]:
            emptyword.pop()
            popcount+=1
        else:
            emptyword.append(word[i])
                     


# In[24]:


if popcount%2==0:
    print('No')
else:
    print('Yes')


# In[ ]:





