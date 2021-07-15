import sys
from math import *
from fractions import gcd
from random import * # randint(inclusive,inclusive)
readints=lambda:list(map(int, input().strip('\n').split()))
from itertools import permutations, combinations
s = "abcdefghijklmnopqrstuvwxyz"
# print('', end=" ")
# for i in {1..5}; do echo "hi"; done




n,k=readints()
s=input()

g=[0]*n
for i in range(n):
    if s[i]=='0':
        g[i]=i
    else:
        g[i]=g[i-1]


def f(hop):
    at=0
    used=0
    while used<k-2 and n-1-at>hop:
        to=g[at+hop]
        if to==at:
            break
        used+=1
        at=to

    if n-1-at>hop:
        return False
    return True


lo=-1
hi=n+1

while hi-lo>1:
    mid=(lo+hi)//2
    if f(mid):
        hi=mid
    else:
        lo=mid

print(hi-1)

