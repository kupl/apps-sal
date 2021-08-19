N = int(input())
A = list(map(int, input().split()))
p = list(range(N))
p.sort(key=lambda i: A[i], reverse=True)
dp = [[0] * (N + 1) for _ in range(N + 1)]
for i in range(N):
    for j in range(i + 1):
        pi = p[i]
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j] + A[pi] * (N - i + j - 1 - pi))
        dp[i + 1][j + 1] = dp[i][j] + A[pi] * (pi - j)
print(max(dp[N]))
