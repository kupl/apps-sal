import sys
from collections import deque, defaultdict, Counter
from itertools import accumulate, product, permutations, combinations
from operator import itemgetter
from bisect import bisect_left, bisect_right
from heapq import heappop, heappush
from math import ceil, floor, sqrt, gcd, inf
from copy import deepcopy
import numpy as np
import scipy as sp

INF = inf
MOD = 1000000007

n = int(input())
A = [[int(i) for i in input().split()]for j in range(n)]    # nは行数

tmp = 0
res = 0

ul = INF
ur = INF
bl = INF
br = INF
ul_index = 0
ur_index = 0
bl_index = 1
br_index = 1
for i in range(n):
    x, y = A[i]
    if x + 10e9 - y <= ul:
        ul = x + 10e9 - y
        ul_index = i
    if 10e9 - x + 10e9 - y <= ur:
        ur = 10e9 - x + 10e9 - y
        ur_index = i
    if x + y <= bl:
        bl = x + y
        bl_index = i
    if 10e9 - x + y <= br:
        br = 10e9 - x + y
        br_index = i
res = max(abs(A[ul_index][0] - A[br_index][0]) + abs(A[ul_index][1] - A[br_index][1]), abs(A[ur_index][0] - A[bl_index][0]) + abs(A[ur_index][1] - A[bl_index][1]))

print(res)

