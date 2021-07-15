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
p = L()
mi = sys.maxsize
cnt = 0
for i in p:
    if i <= mi:
        cnt += 1
        mi = i
print(cnt)
