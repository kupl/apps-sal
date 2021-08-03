from collections import Counter, defaultdict, deque
from heapq import heappop, heappush, heapify
import sys
import bisect
import math
import itertools
import fractions
sys.setrecursionlimit(10**8)
mod = 10**9 + 7
INF = float('inf')
def inp(): return int(sys.stdin.readline())
def inpl(): return list(map(int, sys.stdin.readline().split()))


x, t = inpl()
print(max(x - t, 0))
