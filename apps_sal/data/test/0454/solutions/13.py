import os
import sys

import numpy as np

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(2147483647)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7

N, K = list(map(int, sys.stdin.readline().split()))

# # A: {1, 2, ..., N}
# # B: 作る数列
# # dp[i, k, a, b]:
# # i まで見て
# # 奇妙さが k で
# # A のうち場所が決まってない数が a
# # B のうち入れる A が決まってない数が b
# dp = np.zeros((N + 1, K + 1, N + 1, N + 1), dtype=int)
# dp[0, 0, 0, 0] = 1
# for i in range(N):
#     for k in range(K + 1):
#         for a in range(N + 1):
#             for b in range(N + 1):
#                 # A[i] を B[i] に持ってく
#                 if k + a + b <= K:
#                     dp[i + 1][k + a + b][a][b] += dp[i][k][a][b]
#                 # 場所が決まってない A を B[i] に入れる
#                 # 場所が決まってない B に A[i] を入れる
#                 if a > 0 and b > 0 and k + a + b - 2 <= K:
#                     dp[i + 1][k + a + b - 2][a - 1][b - 1] += dp[i][k][a][b] * a * b
#                 # 片方だけ決める
#                 if a > 0 and b > 0 and k + a + b <= K:
#                     dp[i + 1][k + a + b][a][b] += dp[i][k][a][b] * a
#                     dp[i + 1][k + a + b][a][b] += dp[i][k][a][b] * b
#                 # 両方決めない
#                 if k + a + b + 2 <= K and a + 1 < N and b + 1 < N:
#                     dp[i + 1][k + a + b + 2][a + 1][b + 1] += dp[i][k][a][b]
# print(dp[-1][K][0][0] % MOD)


# # a と b は常に同じなのでまとめる
# dp = np.zeros((N + 1, K + 1, N + 1), dtype=int)
# dp[0, 0, 0] = 1
# for i in range(N):
#     for k in range(K + 1):
#         for a in range(N + 1):
#             # A[i] を B[i] に持ってく
#             if k + a * 2 <= K:
#                 dp[i + 1][k + a * 2][a] += dp[i][k][a]
#             # 場所が決まってない A を B[i] に入れる
#             # 場所が決まってない B に A[i] を入れる
#             if a > 0 and k + a * 2 - 2 <= K:
#                 dp[i + 1][k + a * 2 - 2][a - 1] += dp[i][k][a] * (a ** 2)
#             # 片方だけ決める
#             if a > 0 and k + a * 2 <= K:
#                 dp[i + 1][k + a * 2][a] += dp[i][k][a] * a * 2
#             # 両方決めない
#             if k + a * 2 + 2 <= K and a + 1 < N:
#                 dp[i + 1][k + a * 2 + 2][a + 1] += dp[i][k][a]
#     dp[i + 1] %= MOD
# print(dp[-1][K][0] % MOD)

# a と b は常に同じなのでまとめる
dp = np.zeros((N + 1, K + 1, N + 1), dtype=int)
dp[0, 0, 0] = 1
for i in range(N):
    for a in range(N + 1):
        k = np.arange(K + 1)
        # A[i] を B[i] に持ってく
        if a == 0:
            dp[i + 1, :, a] += dp[i, :, a]
        else:
            dp[i + 1, a * 2:, a] += dp[i, :-(a * 2), a]

        # 場所が決まってない A を B[i] に入れる
        # 場所が決まってない B に A[i] を入れる
        if a * 2 - 2 == 0:
            dp[i + 1, :, a - 1] += dp[i, :, a] * (a ** 2)
        elif a * 2 - 2 > 0:
            dp[i + 1, a * 2 - 2:, a - 1] += dp[i, :-(a * 2 - 2), a] * (a ** 2)

        # 片方だけ決める
        if a > 0:
            dp[i + 1, a * 2:, a] += dp[i, :-(a * 2), a] * a * 2

        # 両方決めない
        if a + 1 < N:
            dp[i + 1, a * 2 + 2:, a + 1] += dp[i, :-(a * 2 + 2), a]
    dp[i + 1] %= MOD
print((dp[-1][K][0] % MOD))

# ans = 0
# for li in itertools.permutations(range(N)):
#     ans += abs(np.array(li) - np.arange(N)).sum() == K
#     if abs(np.array(li) - np.arange(N)).sum() == K:
#         print(np.array(li) + 1)
# print(ans)

