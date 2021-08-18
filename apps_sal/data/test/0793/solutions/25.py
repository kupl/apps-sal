import os
import sys

import numpy as np

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(2147483647)
INF = float("inf")

MOD = 10 ** 9 + 7
N, M = list(map(int, sys.stdin.readline().split()))
S = list(map(int, sys.stdin.readline().split()))
T = list(map(int, sys.stdin.readline().split()))
S = np.array([-1] + S)
T = np.array([-1] + T)


cumsum = np.ones(len(T), dtype=int)
for i in range(1, len(S)):
    cumsum[1:] += ((T == S[i])[1:] * cumsum[:-1] % MOD).cumsum()
    cumsum %= MOD
print((cumsum[-1]))
