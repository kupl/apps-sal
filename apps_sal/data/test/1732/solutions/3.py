from decimal import Decimal
import sys
import math
import io
import os
from bisect import bisect_left as bl, bisect_right as br, insort
from heapq import heapify, heappush, heappop
from collections import defaultdict as dd, deque, Counter
def data(): return sys.stdin.readline().strip()
def mdata(): return list(map(int, data().split()))
def outl(var): sys.stdout.write(' '.join(map(str, var)) + '\n')
def out(var): sys.stdout.write(str(var) + '\n')


mod = int(1e9) + 7
INF = float('inf')

n = int(data())
l = mdata()
c = mdata()
d = dict()
for i in range(n):
    if d.get(l[i]):
        d[l[i]] = min(d[l[i]], c[i])
    else:
        d[l[i]] = c[i]
for i in l:
    lis = list(d.keys())
    for j in lis:
        g = math.gcd(i, j)
        if d.get(g):
            d[g] = min(d[g], d[i] + d[j])
        else:
            d[g] = d[i] + d[j]
if 1 in d:
    out(d[1])
else:
    out(-1)
