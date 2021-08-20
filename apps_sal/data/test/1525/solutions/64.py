import sys
readline = sys.stdin.readline
(H, W, K) = list(map(int, readline().split()))
DIV = 1000000007
LINE = [-1] * (W - 1)
for i in range(W - 1):
    dp = [[0] * 2 for j in range(W - 1)]
    if i == 0:
        dp[0][0] = 0
        dp[0][1] = 1
    else:
        dp[0][0] = 1
        dp[0][1] = 1
    for j in range(1, W - 1):
        if j == i:
            dp[j][0] = 0
            dp[j][1] = dp[j - 1][0]
        else:
            dp[j][0] += dp[j - 1][0] + dp[j - 1][1]
            dp[j][1] += dp[j - 1][0]
    LINE[i] = dp[-1][0] + dp[-1][1]
    LINE[i] %= DIV
POINT = [-1] * W
for i in range(W):
    dp = [[0] * 2 for j in range(W)]
    if i - 1 == 0 or i == 0:
        dp[0][0] = 1
        dp[0][1] = 0
    else:
        dp[0][0] = 1
        dp[0][1] = 1
    for j in range(1, W):
        if j == i - 1 or j == i:
            dp[j][1] = 0
            dp[j][0] += dp[j - 1][0] + dp[j - 1][1]
        else:
            dp[j][0] += dp[j - 1][0] + dp[j - 1][1]
            if j == W - 1:
                dp[j][1] = 0
            else:
                dp[j][1] += dp[j - 1][0]
    POINT[i] = dp[-1][0] + dp[-1][1]
    POINT[i] %= DIV
dp = [[0] * W for i in range(H + 1)]
dp[0][0] = 1
for i in range(1, len(dp)):
    for j in range(W):
        if j - 1 >= 0:
            dp[i][j] += dp[i - 1][j - 1] * LINE[j - 1]
        dp[i][j] += dp[i - 1][j] * POINT[j]
        if j + 1 < W:
            dp[i][j] += dp[i - 1][j + 1] * LINE[j]
        dp[i][j] %= DIV
print(dp[H][K - 1])
