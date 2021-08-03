import numpy as np
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)

N, K = map(int, input().split())

# ある線を、左にまたぐ数の集合、右にまたぐ数の集合など

MOD = 10 ** 9 + 7

dp = np.zeros((N + 1, N * N + 1), dtype=np.int64)  # ある線をまたぐ（左右）個数、これまでの合計点、場合の数
dp[0, 0] = 1
for n in range(1, N + 1):
    prev = dp
    dp = np.zeros_like(prev)
    for m in range(N):
        dp[m, m:] += prev[m, :N * N + 1 - m]  # その点を不動点にしてそのまま
        dp[m, m:] += prev[m, :N * N + 1 - m] * m  # どれかをそこに留めてのこりを右に
        dp[m + 1, m + 1:] += (m + 1) * prev[m, :N * N - m]  # その点ごと全部右に。左に流す方をどれか残す
        dp[m, m:] += prev[m, :N * N + 1 - m] * m  # xを左に、左から来たのは全て右に
        dp[m, m:] += (m + 1) * prev[m + 1, :N * N + 1 - m]  # その点ごと全部右に。左に流す方をどれか残す
    dp %= MOD

if K & 1:
    answer = 0
else:
    answer = dp[0, K // 2]

print(answer)
