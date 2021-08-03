from collections import Counter
from collections import deque, defaultdict
import itertools as it
from math import gcd, floor, ceil, factorial
import sys
input = sys.stdin.readline
# sys.setrecursionlimit(10**6)


def inp():
    return int(input())


def inps():
    return input().rstrip()


def inpl():
    return list(map(int, input().split()))


def inpls():
    return list(map(str, input().split()))

# import decimal
# from decimal import Decimal
# decimal.getcontext().prec = 10


# from heapq import heappush, heappop, heapify
# import math


def lcd(a, b):
    return a * b // gcd(a, b)


def chmin(dp, i, x):
    if x < dp[i]:
        dp[i] = x
        return True
    return False


def chmax(dp, i, x):
    if x > dp[i]:
        dp[i] = x
        return True
    return False

# ---------------------------------------


N, S = input().split()
N = int(N)
S = S.rstrip()

A = [0] * (N + 1)
T = [0] * (N + 1)
C = [0] * (N + 1)
G = [0] * (N + 1)
for i in range(N):
    s = S[i]
    A[i + 1] = A[i] + (1 if s == "A" else 0)
    T[i + 1] = T[i] + (1 if s == "T" else 0)
    C[i + 1] = C[i] + (1 if s == "C" else 0)
    G[i + 1] = G[i] + (1 if s == "G" else 0)

ans = 0
for i in range(N):
    j = i + 2
    while j <= N:
        if A[j] - A[i] == T[j] - T[i] and C[j] - C[i] == G[j] - G[i]:
            ans += 1
        j += 2

print(ans)
