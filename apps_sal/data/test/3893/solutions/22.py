import re, sys, math, string, operator, functools, fractions, collections
from random import *
sys.setrecursionlimit(10**7)
dX= [-1, 1, 0, 0,-1, 1,-1, 1]
dY= [ 0, 0,-1, 1, 1,-1,-1, 1]
RI=lambda: list(map(int,input().split()))
RS=lambda: input().rstrip().split()
mod=1e9+7
#################################################
x1,y1 = RI()
x2,y2 = RI()
def sign(x):
    return x<0
n=RI()[0]
ans=0
for i in range(n):
    a,b,c=RI()
    if sign(a*x1+b*y1+c)!=sign(a*x2+b*y2+c):
        ans+=1
print(ans)

