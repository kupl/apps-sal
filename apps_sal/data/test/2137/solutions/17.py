import sys
import math
import bisect
import itertools
from collections import Counter

d = {}
s = {}
n, a, b = list(map(int, sys.stdin.readline().strip().split(' ')))
for n0 in range(n):
    x, vxi, vyi = list(map(int, sys.stdin.readline().strip().split(' ')))
    curr = a * vxi - vyi
    if curr in d:
        if (vxi, vyi) in d[curr]:
            d[curr][(vxi, vyi)] += 1
        else:
            d[curr][(vxi, vyi)] = 1
        s[curr] += 1
    else:
        d[curr] = {(vxi, vyi): 1}
        s[curr] = 1

ans = 0
for k, v in list(d.items()):
    for vxy, q in list(v.items()):
        ans += (s[k] - q) * q
print(ans)
