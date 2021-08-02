import collections
import math
import sys


def N():
    return int(input())


def L():
    return list(map(int, input().split()))


def NL(n):
    return [list(map(int, input().split())) for i in range(n)]


mod = pow(10, 9) + 7

#import numpy as np

n, m = L()
sc = NL(m)
num = [0] * n
if n == 1:
    num[0] = 0
else:
    num[0] = 1
flag = [True] * n
for s, c in sc:
    if s == 1:
        if c == 0 and n != 1:
            print(-1)
            return
        if flag[0]:
            num[0] = c
            flag[0] = False
        elif num[0] != c:
            print(-1)
            return
    else:
        if flag[s - 1]:
            num[s - 1] = c
            flag[s - 1] = False
        elif (num[s - 1] != c):
            print(-1)
            return

for i in range(n):
    print(num[i], end="")
print()
