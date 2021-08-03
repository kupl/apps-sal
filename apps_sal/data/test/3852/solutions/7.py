from collections import Counter, defaultdict, deque
from heapq import heappop, heappush, heapify
import sys
import bisect
import math
import itertools
import fractions
import copy
sys.setrecursionlimit(10**8)
mod = 10**9 + 7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))


n = inp()
a = inpl()
mx = 0
pl = None
ind = -1
res = []
for i, x in enumerate(a):
    if abs(x) > mx:
        mx = abs(x)
        ind = i
        pl = True if x > 0 else False
if mx == 0:
    print(0)
    return
if not pl:
    mx *= -1
for i in range(n):
    if i == ind:
        continue
    res.append([ind + 1, i + 1])
    a[i] += mx
if pl:
    for i in range(n - 1):
        res.append([i + 1, i + 2])
else:
    for i in range(n - 1)[::-1]:
        res.append([i + 2, i + 1])
print(len(res))
for x in res:
    print(*x)
