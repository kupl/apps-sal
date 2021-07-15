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

s = input()
cnt = 0
pre = 1
ma = 0
for i in range(3):
    if s[i] == 'R' and pre == 1:
        cnt += 1
    elif s[i] == 'R' and pre == 0:
        pre = 1
        cnt = 1
    else:
        cnt = 0
        pre = 0
    ma = max(cnt,ma)
print(ma)
