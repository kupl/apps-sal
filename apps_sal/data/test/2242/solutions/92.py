from decimal import *
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
from functools import reduce
def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))


sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

S = input()
n = len(S)
s = [0]
for i, x in enumerate(S):
    s.append(int(S[i]) * pow(10, n - i - 1, 2019) % 2019)

tmp = 0
t = []
for x in s:
    tmp = (tmp + x) % 2019
    t.append(tmp)

ans = 0
for v in Counter(t).values():
    ans += v * (v - 1) // 2
print(ans)
