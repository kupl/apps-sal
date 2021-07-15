import sys
from math import *
from fractions import gcd
readints=lambda:list(map(int, input().strip('\n').split()))

n=int(input())
s=input()
a=list(readints())
a=[0]+a #1-index

cache={}

def solve(i,j,k):
    if i>j: return 0
    if i==j: return a[k]
    if (i,j,k) in cache: return cache[(i,j,k)]

    best=a[k]+solve(i+1,j,1)
    for x in range(i+1,j+1):
        if s[i]==s[x]:
            best=max(best,solve(i+1,x-1,1)+solve(x,j,k+1))
    #print(i,j,best)
    cache[(i,j,k)]=best
    return best


ans=solve(0,n-1,1)
print(ans)
      

