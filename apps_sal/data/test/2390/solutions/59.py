import sys
import re
import os
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits
from fractions import gcd


def input(): return sys.stdin.readline().strip()
def INT(): return int(input())
def MAP(): return map(int, input().split())
def S_MAP(): return map(str, input().split())
def LIST(): return list(map(int, input().split()))
def S_LIST(): return list(map(str, input().split()))


sys.setrecursionlimit(10 ** 9)
INF = float('inf')
mod = 10 ** 9 + 7

N, C = MAP()
L = [LIST() for i in range(N)]
A = [0] * N
B = [0] * N

X = []
V = []
for x, v in L:
    X.append(x)
    V.append(v)

tmp_v = 0
for i in range(N):
    tmp_v += V[i]
    A[i] = tmp_v - X[i]

tmp_v = 0
for i in range(N - 1, -1, -1):
    tmp_v += V[i]
    B[i] = tmp_v - (C - X[i])

gA = [0] * N
gA[0] = A[0]

for i in range(1, N):
    gA[i] = max(gA[i - 1], A[i])

gB = [0] * N
gB[N - 1] = B[N - 1]

for i in range(N - 2, -1, -1):
    gB[i] = max(gB[i + 1], B[i])

a = max(A)
b = max(B)
c, d = 0, 0
if N > 1:
    c = max([A[i] - X[i] + gB[i + 1] for i in range(0, N - 1)])
    d = max([B[i] - (C - X[i]) + gA[i - 1] for i in range(N - 1, 0, -1)])
print(max(a, b, c, d, 0))
