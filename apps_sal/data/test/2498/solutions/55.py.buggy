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
INF = 10**6  # float('inf')
#mod = 10 ** 9 + 7
mod = 998244353
#from decimal import *
#import numpy as np
#decimal.getcontext().prec = 10

N, M = MAP()
a = LIST()

A = sorted([x // 2 for x in a], reverse=True)

lcm = A[-1]
for x in A:
    lcm = lcm * x // gcd(lcm, x)

r = lcm // A[0]
n = M // A[0]


for x in A:
    if lcm // x % 2 == 0:
        print(0)
        return
# 2p+1が1<=2p+1<=n の範囲で rの倍数となるpの個数
if r % 2 == 0:
    print(0)
else:
    print(n // r - n // (2 * r))
