import sys
from math import *
from fractions import gcd
readints=lambda:list(map(int, input().strip('\n').split()))

n = int(input())
a = list(readints())

s = sum(a)
m = min(a)

best = s
for x in a:
    for d in range(1,x+1):
        if x%d==0:
            dx=x/d
            dm=m*d
            s2 = s-x-m+dx+dm
            best = min(best,s2)

best=int(best)

print(best)
    

