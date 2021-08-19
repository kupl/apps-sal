# 想定解法
N, A = list(map(int, input().split()))
X = sorted(list(map(int, input().split())))
xm = max(X)
xm = max(xm, A)
for i in range(N):
    X[i] -= A
#print(X, xm)
dp = [[0] * (2 * N * xm + 1) for i in range(N + 1)]
dp[0][N * xm] = 1

for i in range(1, N + 1):
    for j in range(2 * N * xm + 1):
        if 0 <= j - X[i - 1] <= 2 * N * xm:
            dp[i][j] = dp[i - 1][j] + dp[i - 1][j - X[i - 1]]
        else:
            dp[i][j] = dp[i - 1][j]

print((dp[N][N * xm] - 1))
