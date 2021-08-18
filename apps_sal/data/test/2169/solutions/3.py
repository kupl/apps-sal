import sys
import re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, tan, asin, acos, atan, radians, degrees
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
def MAP(): return map(int, input().split())
def LIST(): return list(map(int, input().split()))
def ZIP(n): return zip(*(MAP() for _ in range(n)))


sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10**9 + 7

H, W, D = MAP()
A = [LIST() for _ in range(H)]

dic = defaultdict(tuple)

for y in range(H):
    for x in range(W):
        dic[A[y][x]] = (y + 1, x + 1)

power = [[] for _ in range(D)]
for i in range(1, H * W + 1):
    if i <= D:
        power[i % D].append(0)
    else:
        idx = i % D
        tmp = abs(dic[i][0] - dic[i - D][0]) + abs(dic[i][1] - dic[i - D][1])
        power[i % D].append(tmp)

power_acc = []
for x in power:
    power_acc.append(list(accumulate(x)))
power_acc[0].insert(0, 0)

Q = INT()
for _ in range(Q):
    L, R = MAP()
    print(power_acc[R % D][R // D] - power_acc[L % D][L // D])
