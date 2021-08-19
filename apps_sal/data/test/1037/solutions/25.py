N = int(input())
_A = sorted(enumerate(map(int, input().split()), 1), key=lambda x: x[1], reverse=True)
dp = [[0] * (N + 1) for i in range(N + 1)]
for i in range(1, N + 1):
    (k, Ak) = _A[i - 1]
    if N - i - k < 0:
        break
    dp[0][i] = dp[0][i - 1] + (N - i + 1 - k) * Ak
for i in range(1, N + 1):
    (k, Ak) = _A[i - 1]
    if k - i < 0:
        break
    dp[i][0] = dp[i - 1][0] + (k - i) * Ak
for x in range(1, N + 1):
    for y in range(1, N - x + 1):
        (k, val) = _A[x + y - 1]
        dp[x][y] = max(dp[x - 1][y] + abs(k - x) * val, dp[x][y - 1] + abs(N - y - k + 1) * val)
print(int(max((dp[i][N - i] for i in range(N + 1)))))
