import math

h, w = map(int, input().split())
a = [list(map(int, input().split())) for i in range(h)]
b = [list(map(int, input().split())) for i in range(h)]

diff = [[abs(x - y) for x, y in zip(ar, br)] for ar, br in zip(a, b)]

M = 80 * (h + w)
dp = [[0 for j in range(w)] for i in range(h)]
dp[0][0] = 1 << (diff[0][0] + M)
for i in range(h):
    for j in range(w):
        if i > 0:
            dp[i][j] |= (dp[i - 1][j] << diff[i][j]) | (dp[i - 1][j] >> diff[i][j])
        if j > 0:
            dp[i][j] |= (dp[i][j - 1] << diff[i][j]) | (dp[i][j - 1] >> diff[i][j])
        dp[i][j] &= (1 << (M * 2)) - 1
for k in range(M):
    if (dp[h - 1][w - 1] >> (k + M)) & 1 == 1:
        print(k)
        break
