#!/usr/bin/env python
# coding: utf-8

# In[11]:


N,M = list(map(int, input().split()))


# In[12]:


def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]


# In[14]:


for x in make_divisors(M)[::-1]:
    if M//x >= N:
        ans = x
        break
print(ans)


# In[ ]:





