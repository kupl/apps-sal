#!/usr/bin/env python
# coding: utf-8

# In[21]:


import copy
r = input().split()
n = int(r[0])
m = int(r[1])
ar = [[] for i in range(n)]
#print(ar)
for i in range(m):
   r = input().split()
   a = int(r[0]) 
   b = int(r[1])
   ar[a - 1].append(b - 1)
#   print(ar)
train = []
result = []
for i in range(n):
    count = m
    arr = copy.deepcopy(ar)
    time = copy.deepcopy(ar)
    ind = i
    res = 0
    for j in range(n):
        for k in range(len(arr[j])):
            if arr[j][k] >= j:
                time[j][k] = arr[j][k] - j
            else:
                time[j][k] = n - 1 - j + arr[j][k] + 1
#print(time)                
    while (count != 0) or (len(train) != 0):
        if len(arr[ind]) != 0:
            train.append(arr[ind][time[ind].index(max(time[ind]))])
#        print(time[ind].index(max(time[ind])))
#        print(max(time[ind]))
            del arr[ind][time[ind].index(max(time[ind]))]
            del time[ind][time[ind].index(max(time[ind]))]
#        print(arr)
#        print(time)
            count -= 1
#    print(train)    
        while train.count(ind) != 0:
            train.remove(ind)
#        print(train)
        ind += 1
        if ind == len(arr): 
            ind = 0
        res += 1
    result.append(res - 1)    
#    print(ind)
#    print(res) 
print(' '.join(map(str, result)))
#print(ind)
    


# 

# ## 

# In[ ]:





