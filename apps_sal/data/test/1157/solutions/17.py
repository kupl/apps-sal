def ii(): return int(input())
def si(): return input()
def mi(): return map(int,input().split())
def li(): return list(mi())

import math

n=ii()
a=li()
l=[0]*200005
s=ans=0
t=(n*(n+1))//2
for i in range(n):
    if a[i]<0:
        l[i]=1 
    c,d=1,0 
for i in range(n):
    s+=l[i]
    if s%2!=0:
        ans+=d 
        d+=1 
    else:
        ans+=c 
        c+=1
print(t-ans,ans)
