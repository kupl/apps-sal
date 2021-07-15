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

# # dp[i][j]: S[i] と T[j] で終わる組み合わせの数
# # S[i] != T[j] のとき 0
# # S[i] == T[j] のとき、sum(dp[:i][:j])
# dp = np.zeros((len(S), len(T)), dtype=int)
# dp[0][0] = 1
# # dp の二次元累積和
# cumsum = np.ones(len(T), dtype=int)
# for i in range(1, len(S)):
#     for j in range(1, len(T)):
#         if S[i] != T[j]:
#             continue
#         # dp[i][j] = dp[:i, :j].sum() % MOD
#         dp[i][j] = cumsum[j - 1] % MOD
#     cumsum += dp[i].cumsum()
#     cumsum %= MOD
# print(cumsum[-1])


cumsum = np.ones(len(T), dtype=int)
for i in range(1, len(S)):
    cumsum[1:] += ((T == S[i])[1:] * cumsum[:-1] % MOD).cumsum()
    cumsum %= MOD
print((cumsum[-1]))

