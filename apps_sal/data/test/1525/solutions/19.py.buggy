import itertools
H, W, K = map(int, input().split())
dp = [[0] * W for i in range(H + 1)]
dp[0][0] = 1
if W == 1:
    print(1)
    return

A = list(itertools.product([0, 1], repeat=W - 1))

B = []
for i in A:
    x = 0
    for j in range(W - 2):
        if i[j] == 1 and i[j + 1] == 1:
            x = 1
    if x == 0:
        B.append(i)

D = [[0, 0, 0] for i in range(W)]
for i in B:
    for j in range(W - 1):
        if i[j] == 1:
            D[j + 1][0] += 1
            D[j][2] += 1
        if j == 0 and i[j] == 0:
            D[j][1] += 1
        if j == W - 2 and i[j] == 0:
            D[j + 1][1] += 1
        if j < W - 2:
            if i[j] == 0 and i[j + 1] == 0:
                D[j + 1][1] += 1
dp = [[0] * W for i in range(H + 1)]
mod = 10**9 + 7
dp[0][0] = 1
for i in range(H):
    for j in range(W):
        if j == 0:
            dp[i + 1][j] = dp[i][j] * D[j][1] + dp[i][j + 1] * D[j][2]
        elif j == W - 1:
            dp[i + 1][j] = dp[i][j] * D[j][1] + dp[i][j - 1] * D[j][0]
        else:
            dp[i + 1][j] = dp[i][j] * D[j][1] + dp[i][j - 1] * D[j][0] + dp[i][j + 1] * D[j][2]
        dp[i + 1][j] %= mod
print(dp[-1][K - 1])
