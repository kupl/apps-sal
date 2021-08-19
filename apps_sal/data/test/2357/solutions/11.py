from math import *
from collections import *
import sys
sys.setrecursionlimit(10 ** 9)
t = int(input())
for y in range(t):
    n = int(input())
    l = list(map(int, input().split()))
    d = dict()
    m = 1000000000.0
    for i in range(n):
        if l[i] not in d:
            d[l[i]] = [i]
        else:
            d[l[i]].append(i)
            m = min(m, i - d[l[i]][-2] + 1)
    if m == 1000000000.0:
        print(-1)
    else:
        print(m)
