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

h, w, k = [int(i) for i in input().split()]
C = [input() for j in range(h)] # nは行数

tmp = 0
res = 0

for r in range(h):
    for c in range(w):
        if C[r][c] == "#":
            tmp += 1

for i in range(2 ** h):
    for j in range(2 ** w):
        rs = f"{i:0{h}b}"
        cs = f"{j:0{w}b}"
        tmp_2 = 0
        for r in range(h):
            for c in range(w):
                if (rs[r] == "1" or cs[c] == "1") and C[r][c] == "#":
                    tmp_2 += 1
        if tmp - tmp_2 == k:
            res += 1

print(res)

