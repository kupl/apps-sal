from collections import Counter, defaultdict, deque
from heapq import heappop, heappush
from bisect import bisect_left, bisect_right
import sys
import math
import itertools
import fractions
sys.setrecursionlimit(10 ** 8)
mod = 10 ** 9 + 7
INF = float('inf')


def inp():
    return int(sys.stdin.readline())


def inpl():
    return list(map(int, sys.stdin.readline().split()))


(n, a, b) = inpl()
dl = 1
for i in range(a):
    dl *= n - i
    dl %= mod
for i in range(a):
    dl *= pow(a - i, mod - 2, mod)
    dl %= mod
vv = 1
for i in range(b):
    vv *= n - i
    vv %= mod
for i in range(b):
    vv *= pow(b - i, mod - 2, mod)
    vv %= mod
res = pow(2, n, mod) - dl - vv - 1
print(res % mod)
