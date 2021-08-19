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
def MAP(): return list(map(int, input().split()))
def LIST(): return list(map(int, input().split()))
def ZIP(n): return list(zip(*(MAP() for _ in range(n))))


sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7
#mod = 998244353
#import numpy as np
#decimal.getcontext().prec = 10

H, W, D = MAP()
A = [LIST() for _ in range(H)]
Q = INT()
LR = [LIST() for _ in range(Q)]

dic = [[] for _ in range(D)]

for y in range(H):
    for x in range(W):
        # print(dic)
        dic[A[y][x] % D].append([A[y][x], y, x])

for lis in dic:
    lis.sort(key=lambda x: x[0])

for lis in dic:
    lis[0][0] = 0
    for i in range(len(lis)):
        if i == len(lis) - 1:
            break
        point = (lis[i][1], lis[i][2])
        dist_point = (lis[i + 1][1], lis[i + 1][2])
        lis[i + 1][0] = lis[i][0] + abs(point[0] - dist_point[0]) + abs(point[1] - dist_point[1])

# print(dic)
for L, R in LR:
    print((dic[R % D][ceil(R / D) - 1][0] - dic[R % D][ceil(L / D) - 1][0]))
