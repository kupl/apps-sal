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
def MAP(): return list(map(int, input().split()))
def LIST(): return list(map(int, input().split()))
def TUPLE(): return tuple(map(int, input().split()))
def ZIP(n): return list(zip(*(MAP() for _ in range(n))))


sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7
#mod = 998244353
#from decimal import *
#import numpy as np
#decimal.getcontext().prec = 10

s = input()
x, y = MAP()

cnt = [[] for _ in range(2)]

limit = 8000

flg = 0
cnt_F = 0
for char in s:
    if char == "F":
        cnt_F += 1

    elif char == "T":
        if cnt_F:
            cnt[flg].append(cnt_F)
        flg ^= 1
        cnt_F = 0

if cnt_F:
    cnt[flg].append(cnt_F)

for i in range(2):
    if not cnt[i]:
        cnt[i].append(0)

UD = cnt[1][1:]
start_UD = cnt[1][0]

dp_UD = [0] * (2 * limit + 1)
dp_UD[start_UD] = 1
dp_UD[-start_UD] = 1

for k in UD:
    dp_UD2 = [0] * (2 * limit + 1)
    for i in range(-limit, limit + 1):
        if dp_UD[i]:
            dp_UD2[i - k] = 1
            dp_UD2[i + k] = 1
    dp_UD = dp_UD2

LR = cnt[0][1:]
start_LR = cnt[0][0]

dp_LR = [0] * (2 * limit + 1)
dp_LR[start_LR] = 1
if s[0] == "T":
    dp_LR[-start_LR] = 1

for k in LR:
    dp_LR2 = [0] * (2 * limit + 1)
    for i in range(-limit, limit + 1):
        if dp_LR[i]:
            dp_LR2[i - k] = 1
            dp_LR2[i + k] = 1
    dp_LR = dp_LR2

if dp_LR[x] and dp_UD[y]:
    print("Yes")
else:
    print("No")
