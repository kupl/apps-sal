

import sys
n,k=list(map(int,input().split()))

l=list(map(int,input().split()))
t=list(map(int,input().split()))
if(k>n):
    print(sum(l))
    return
base=0
for i in range(n):
    if(t[i]==1):
        base+=l[i]
        l[i]=0
max1=0
cur=sum(l[:k])
max1=cur
for i in range(k,n):
    cur-=l[i-k]
    cur+=l[i]
    max1=max(cur,max1)
print(max1+ base)


