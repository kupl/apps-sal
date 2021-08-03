from collections import Counter, defaultdict, deque
from heapq import heappop, heappush
from bisect import bisect_left, bisect_right
import sys
import math
import itertools
import fractions
sys.setrecursionlimit(10**8)
mod = 10**9 + 7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))


s = input()
res = 0
for x in s:
    if x == '+':
        res += 1
    else:
        res -= 1
print(res)
