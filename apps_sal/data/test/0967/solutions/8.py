import re, sys, string, operator, functools, fractions, collections
from random import *
sys.setrecursionlimit(10**7)
dX= [-1, 1, 0, 0,-1, 1,-1, 1]
dY= [ 0, 0,-1, 1, 1,-1,-1, 1]
RI=lambda: list(map(int,input().split()))
RS=lambda: input().rstrip().split()
mod=1e9+7
eps=1e-6
#################################################
n=RI()[0]
a=RI()
ans=1
for i in range(n-1,0,-1):
    if a[i-1]>a[i]:
        break
    ans+=1
print(n-ans)

