import sys
import re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees  # , log2
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
from fractions import gcd
from heapq import heappush, heappop
from functools import reduce
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return list(map(int, input().split()))
def LIST(): return list(map(int, input().split()))
def ZIP(n): return list(zip(*(MAP() for _ in range(n))))


sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10**9 + 7
#from decimal import *

N, M = MAP()
AB = [LIST() for _ in range(N)]
AB.sort(key=lambda x: x[0])

ans = 0
i = 0
B = []
for j in range(1, M + 1):
    while i < N and AB[i][0] <= j:
        heappush(B, -AB[i][1])
        i += 1
    if B:
        ans += -heappop(B)

print(ans)
