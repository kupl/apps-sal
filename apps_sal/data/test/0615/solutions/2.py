import sys
import re
from collections import deque, defaultdict, Counter
from math import ceil, sqrt, hypot, factorial, pi, sin, cos, radians
from heapq import heappop, heappush, heapify, heappushpop
from itertools import permutations, combinations, product, accumulate
from operator import itemgetter, mul
from copy import deepcopy
from string import ascii_lowercase, ascii_uppercase, digits


def input():
    return sys.stdin.readline().strip()


def INT():
    return int(input())


def MAP():
    return list(map(int, input().split()))


def LIST():
    return list(map(int, input().split()))


sys.setrecursionlimit(10 ** 9)
INF = float('inf')
MOD = 10 ** 9 + 7
N = INT()
A = LIST()
B = list(accumulate(A))
(l, c, r) = (0, 1, 2)
P = sum(A[:l])
Q = sum(A[l:c])
R = sum(A[c:r])
S = sum(A[r:])
ans = INF
for c in range(1, N - 1):
    while True:
        if abs(P - Q) < abs(P + A[l] - (Q - A[l])):
            break
        if l == c - 1:
            break
        P += A[l]
        Q -= A[l]
        l += 1
    while True:
        if abs(R - S) < abs(R + A[r] - (S - A[r])):
            break
        if r == N - 1:
            break
        R += A[r]
        S -= A[r]
        r += 1
    ans = min(max(P, Q, R, S) - min(P, Q, R, S), ans)
    Q += A[c]
    R -= A[c]
print(ans)
