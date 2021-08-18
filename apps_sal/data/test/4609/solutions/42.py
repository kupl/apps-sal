from decimal import ROUND_HALF_UP, Decimal
from collections import deque, Counter, defaultdict
from bisect import bisect_left as bileft, bisect_right as biright
from functools import lru_cache
from math import sqrt, ceil
import sys
mod = 10**9 + 7
inf = float("inf")
def input(): return sys.stdin.readline().strip()


sys.setrecursionlimit(11451419)

n = int(input())
A = [int(input()) for i in range(n)]
C = Counter(A)
print(len([i for i in C.values() if i % 2 == 1]))
