from collections import Counter, defaultdict, deque
from heapq import heappop, heappush, heapify
import sys
import bisect
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


k = inp()
b = (k - 1) // 50 + 50
r = k % 50
l = 50 - r
a = b - r - 1
if r == 0:
    a = b
print(50)
res = [-1] * 50
for i in range(50):
    if i < l:
        res[i] = a
    else:
        res[i] = b
print(*res)
