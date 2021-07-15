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

N, K = mi()

ans = 0
ls = []
for i in range(-N+1, N):
    if K-i<N and K-i>=-N+1:
        A = i
        B = K-A
        ans += ((N-abs(B))*(N-abs(A)))
print(ans)
