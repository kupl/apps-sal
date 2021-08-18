
import sys
readline = sys.stdin.readline

DIV = 10 ** 9 + 7
H, W, K = map(int, readline().split())

P = [0] * max(W - 2 + 1, 3)
P[1], P[2] = 2, 3
for i in range(3, len(P)):
    P[i] = P[i - 1] + P[i - 2]


dp = [[0 for j in range(W)] for i in range(H + 1)]

dp[0][0] = 1


def calc(L, R):
    res = 1
    if 1 < L:
        res *= P[L - 1]
        res %= DIV
    if (W - 1) - (R + 1) >= 1:
        res *= P[(W - 1) - (R + 1)]
        res %= DIV
    return res


for i in range(H):
    for j in range(W):
        if j + 1 < W:
            dp[i + 1][j + 1] += dp[i][j] * calc(j, j + 1)
            dp[i + 1][j + 1] %= DIV
        if j - 1 >= 0:
            dp[i + 1][j - 1] += dp[i][j] * calc(j - 1, j)
            dp[i + 1][j - 1] %= DIV
        dp[i + 1][j] += dp[i][j] * calc(j, j)
        dp[i + 1][j] % DIV


print(dp[H][K - 1] % DIV)
