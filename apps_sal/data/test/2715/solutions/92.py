from collections import Counter, defaultdict, deque
from heapq import heappop, heappush, heapify
from bisect import bisect_left, bisect_right
import sys
import math
import itertools
import fractions
import pprint
sys.setrecursionlimit(10**8)
mod = 10**9 + 7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))


k = inp()
n = 50
x, b = k // 50, k % 50
a = x + (n - 1)
print(n)
for i in range(n):
    if i < b:
        print((n + 1 - b + a))
    else:
        print((a - b))
