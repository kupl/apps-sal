import os
import sys

if os.getenv("LOCAL"):
    sys.stdin = open("_in.txt", "r")

sys.setrecursionlimit(2147483647)
INF = float("inf")
IINF = 10 ** 18
MOD = 10 ** 9 + 7

# 解説AC
N = int(sys.stdin.readline())

# # dp[i][j]: 右からiビット目まで決まってて、vがjとなるパターン数
# dp = [[0] * (N + 1) for _ in range(N.bit_length())]
# # 両方0
# dp[0][0] += 1
# # 片方1
# dp[0][1] += 1
# # 両方1
# dp[0][2] += 1
# for i in range(1, N.bit_length()):
#     for j in range(N + 1):
#         # 両方0
#         dp[i][j] += dp[i - 1][j]
#         # 片方1
#         if j + pow(2, i) <= N:
#             dp[i][j + pow(2, i)] += dp[i - 1][j]
#         # 両方1
#         if j + pow(2, i + 1) <= N:
#             dp[i][j + pow(2, i + 1)] += dp[i - 1][j]
# print(sum(dp[-1]))


# # dp[j]: vがjとなるパターン数
# # 上から決めてく
# dp = [0] * (N + 1)
# # 両方0
# dp[0] = 1
# # 片方1
# dp[1 << (N.bit_length() - 1)] = 1
# for i in reversed(range(N.bit_length() - 1)):
#     for j in reversed(range(N + 1)):
#         # 片方1
#         if j + pow(2, i) <= N:
#             dp[j + pow(2, i)] += dp[j]
#         # 両方1
#         if j + pow(2, i + 1) <= N:
#             dp[j + pow(2, i + 1)] += dp[j]
#     print(dp)
# print(sum(dp))


# # dp[i][j]: 右からiビット目まで決まってて、N-vがjとなるパターン数
# # 上から決めてく
# dp = [[0] * (N + 1) for _ in range(N.bit_length())]
# # 両方0
# dp[-1][-1] = 1
# # 片方1
# dp[-1][N - (1 << (N.bit_length() - 1))] = 1
# for i in reversed(range(N.bit_length() - 1)):
#     for j in reversed(range(N + 1)):
#         # 両方0
#         dp[i][j] += dp[i + 1][j]
#         # 片方1
#         if j - (1 << i) >= 0:
#             dp[i][j - (1 << i)] += dp[i + 1][j]
#         # 両方1
#         if j - (1 << i + 1) >= 0:
#             dp[i][j - (1 << i + 1)] += dp[i + 1][j]
#     print(dp)
# print(sum(dp[0]))

# # dp[i][j]: 右からiビット目まで決まってて、(N>>i)-(v>>i)がjとなるパターン数
# # 上から決めてく
# dp = [[0] * (N * 3) for _ in range(N.bit_length())]
# # 両方0
# dp[-1][1] = 1
# # 片方1
# dp[-1][0] = 1
# for i in reversed(range(N.bit_length() - 1)):
#     for j in reversed(range(N + 1)):
#         if N >> i & 1:
#             # 両方0
#             dp[i][(j << 1) + 1] += dp[i + 1][j]
#             # 片方1
#             dp[i][j << 1] += dp[i + 1][j]
#             if j > 0:
#                 # 両方1
#                 dp[i][(j << 1) - 1] += dp[i + 1][j]
#         else:
#             # 両方0
#             dp[i][j << 1] += dp[i + 1][j]
#             if j > 0:
#                 # 片方1
#                 dp[i][(j << 1) - 1] += dp[i + 1][j]
#                 # 両方1
#                 dp[i][(j << 1) - 2] += dp[i + 1][j]
#     print(dp)
# print(sum(dp[0]))

# dp[i][j]: 右からiビット目まで決まってて、(N>>i)-(v>>i)がjとなるパターン数
# j >= 2 以降は j <= 1 に入ってこないので j == 2 としてまとめる
# 上から決めてく
dp = [[0] * 3 for _ in range(N.bit_length())]
# 両方0
dp[-1][1] = 1
# 片方1
dp[-1][0] = 1
for i in reversed(list(range(N.bit_length() - 1))):
    if N >> i & 1:
        # 両方0
        # dp[i][(j << 1) + 1] += dp[i + 1][j]
        dp[i][1] += dp[i + 1][0]
        dp[i][2] += dp[i + 1][1]
        dp[i][2] += dp[i + 1][2]
        # 片方1
        # dp[i][j << 1] += dp[i + 1][j]
        dp[i][0] += dp[i + 1][0]
        dp[i][2] += dp[i + 1][1]
        dp[i][2] += dp[i + 1][2]
        # 両方1
        # dp[i][(j << 1) - 1] += dp[i + 1][j]
        dp[i][1] += dp[i + 1][1]
        dp[i][2] += dp[i + 1][2]
    else:
        # 両方0
        # dp[i][j << 1] += dp[i + 1][j]
        dp[i][0] += dp[i + 1][0]
        dp[i][2] += dp[i + 1][1]
        dp[i][2] += dp[i + 1][2]
        # 片方1
        # dp[i][(j << 1) - 1] += dp[i + 1][j]
        dp[i][1] += dp[i + 1][1]
        dp[i][2] += dp[i + 1][2]
        # 両方1
        # dp[i][(j << 1) - 2] += dp[i + 1][j]
        dp[i][0] += dp[i + 1][1]
        dp[i][2] += dp[i + 1][2]
    dp[i][0] %= MOD
    dp[i][1] %= MOD
    dp[i][2] %= MOD
print((sum(dp[0]) % MOD))
