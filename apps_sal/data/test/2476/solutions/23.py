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
# https://img.atcoder.jp/abc143/editorial.pdf
N = int(sys.stdin.readline())
A = list(map(int, sys.stdin.readline().split()))

A = np.array(A, dtype=int)
C = np.bincount(A, minlength=N + 2)
D = np.bincount(C, minlength=N + 2)

ld = (D * np.arange(len(D))).cumsum()
ud = D[::-1].cumsum()[::-1]

X = np.arange(1, N + 1, dtype=int)
# L[x]: x 回取れるときの最大の長さ k
L = np.zeros(N + 1, dtype=int)
L[X] = (ld[X] + X * ud[X + 1]) // X

i = len(L) - 1
for k in range(1, N + 1):
    while i > 0 and L[i] < k:
        i -= 1
    print(i)

