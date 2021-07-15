#
from math import ceil,floor
n,q=map(int,input().split())
from sys import stdin,stdout
f=floor(n/2);ce=ceil(n/2)
if n%2==0:
    k=(n//2)*n
else:
    k=((n-1)//2)*(n)+ce
for i in range(q):
    r,c=(int(o) for o in  stdin.readline().split())
    if r%2==1:
        m=((r-1)//2)*n
        if c%2==1:
            print(m+ceil(c/2))
        else:
            print(k+m+floor(c/2))
            
    else:
        m=((r-2)//2)*n
        if c%2==0:
            print(m+ce+floor(c/2))
        else:
            print(k+m+f+ceil(c/2))
