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


def input():
    return sys.stdin.readline().strip()


def INT():
    return int(input())


def MAP():
    return list(map(int, input().split()))


def LIST():
    return list(map(int, input().split()))


def ZIP(n):
    return list(zip(*(MAP() for _ in range(n))))


sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7
(H, W) = MAP()
N = INT()
a = LIST()
cnt = 0
ans = [[-1] * W for _ in range(H)]
tmp = a.pop(0)
color = 1
flg = 0
for i in range(H):
    for j in range(W):
        if i % 2 == 1:
            j = -j - 1
        ans[i][j] = color
        tmp -= 1
        if tmp == 0:
            if not a:
                break
            tmp = a.pop(0)
            color += 1
for i in ans:
    print(' '.join([str(x) for x in i]))
