import os
import sys

import numpy as np

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(2147483647)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7

# 解説AC
# https://twitter.com/maspy_stars/status/1185552225474498560
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

C = list(np.bincount(A).tolist())
C.sort()
deleted = 0
S = N


def solve(k):
    nonlocal S, deleted

    k -= deleted
    while k > 0 and C[-1] > S // k:
        S -= C.pop()
        deleted += 1
        k -= 1
    if k > 0:
        return S // k
    return 0


for k in range(1, N + 1):
    print((solve(k)))

