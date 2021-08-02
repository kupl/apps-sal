import sys
from math import gcd, factorial, ceil, floor, sqrt
from bisect import bisect_left, bisect_right
from copy import deepcopy
from heapq import heapify, heappop, heappush
from itertools import permutations, combinations, product, accumulate
from collections import defaultdict, deque, Counter
from functools import lru_cache
sys.setrecursionlimit(10**8)

ii = lambda: int(input())
mi = lambda: map(int, input().split())
li = lambda: list(map(int, input().split()))

ls = li()
total = sum(ls)
for x in product([0, 1], repeat=4):
    if x == (0, 0, 0, 0):
        continue
    cur = 0
    for i, y in enumerate(x):
        if y == 1: cur += ls[i]
    if 2 * cur == total:
        print('Yes')
        return
print('No')
