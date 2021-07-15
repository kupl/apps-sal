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
s = {}
for i in range(n):
    a = input()
    if a in s:
        s[a] += 1
    else:
        s[a] = 1

s = sorted(s.items(),key=lambda x:x[1],reverse=True)
m = s[0][1]
s2 = []
for i in range(len(s)):
    if s[i][1] == m:
        s2.append(s[i][0])
    else:
        break

s2.sort()
for i in s2:
    print(i)
