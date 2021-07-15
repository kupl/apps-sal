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

lo=-1
hi=n+1



def test(x):
    have=k-1
    last=0
    arr=[]
    for i in range(n):
        if s[i]=='0':
            arr.append(i)

    arr.append(10**9)

    for i in range(1,len(arr)):
        if arr[i]-last-1>x:
            if arr[i-1]==last:
                return False
            if have==0:
                return False
            if arr[i-1]-last-1>x:
                return False
            last=arr[i-1]
            have-=1

    return True



while hi-lo>1:
    mid=(lo+hi)//2
    if test(mid):
        hi=mid
    else:
        lo=mid


print(hi)

