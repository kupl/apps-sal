import sys
import re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees, log2, gcd
from itertools import accumulate, permutations, combinations, combinations_with_replacement, product, groupby
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from bisect import bisect, bisect_left, insort, insort_left
from heapq import heappush, heappop
from functools import reduce, lru_cache
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def TUPLE(): return tuple(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))


sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7
#mod = 998244353
#from decimal import *
#import numpy as np
#decimal.getcontext().prec = 10

N = INT()
P = LIST()

Q = [0] * N
#Q[i]: iの場所
for i, p in enumerate(P):
    Q[p - 1] = i

# print(Q)

check = [0] * N
ans = []

for i in range(N):
    p = Q[i]
    # print("#", i, p)
    if i < p:
        for j in range(p - 1, i - 1, -1):
            if check[j]:
                print(-1)
                return
            check[j] = 1
            ans.append(j + 1)
            P[j], P[j + 1] = P[j + 1], P[j]
            Q[P[j] - 1] -= 1
            Q[P[j + 1] - 1] += 1

for i in range(N - 1, -1, -1):
    if i > p:
        for j in range(p, i):
            if check[j]:
                print(-1)
                return
            check[j] = 1
            ans.append(j + 1)
            P[j], P[j + 1] = P[j + 1], P[j]
            Q[P[j] - 1] -= 1
            Q[P[j + 1] - 1] += 1
            print(P, Q, ans)

if len(ans) < N - 1:
    print(-1)
else:
    print(*ans, sep="\n")
