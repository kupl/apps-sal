
# coding: utf-8

# In[2]:


import sys


# In[3]:


n = int(sys.stdin.readline().strip())
s = sys.stdin.readline().strip()


# In[53]:


balance_max_pos = {}

balance = 0
for i, c in enumerate(s):
    if c == '1':
        balance += 1
    else:
        balance -= 1

    balance_max_pos[balance] = i


# In[58]:


ans = 0
balance = 0
if balance in balance_max_pos:
    ans = max(balance_max_pos[balance] + 1, ans)

for i, c in enumerate(s):
    if c == '1':
        balance += 1
    else:
        balance -= 1

    if balance in balance_max_pos:
        ans = max(balance_max_pos[balance] - i, ans)


# In[59]:


print(ans)


# In[46]:

# In[ ]:
