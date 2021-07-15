def N():
    return int(input())
def L():
    return list(map(int,input().split()))
def NL(n):
    return [list(map(int,input().split())) for i in range(n)]
mod = pow(10,9)+7

#import numpy as np
import sys
import math
import collections

n = N()
l = int(math.log2(n))
su = 0
z = 1
for i in range(l+1):
    su += z
    z *= 2
print(su)
