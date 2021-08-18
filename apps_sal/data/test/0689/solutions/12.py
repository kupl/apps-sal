import sys

import math
import collections
from sys import stdin, stdout, setrecursionlimit
import bisect as bs
setrecursionlimit(2**20)
M = 10**9 + 7

T = int(stdin.readline())

for _ in range(T):
    n = int(stdin.readline())
    d = {}
    for i in range(n):
        s = stdin.readline().strip('\n')
        for c in s:
            if(c not in d):
                d[c] = 0
            d[c] += 1
    res = True
    for c in d:
        if(d[c] % n != 0):
            res = False
            break
    if(res):
        print("YES")
    else:
        print("NO")
