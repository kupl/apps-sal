(N, Ma, Mb) = list(map(int, input().split()))
items = [[int(x) for x in input().split()] for _ in range(N)]
(A, B) = (0, 0)
for (a, b, _) in items:
    A += a
    B += b
dp = [[[float('inf')] * (B + 1) for _ in range(A + 1)] for _ in range(N + 1)]
for i in range(N + 1):
    dp[i][0][0] = 0
for i in range(N):
    (a, b, c) = items[i]
    for j in range(A + 1):
        for k in range(B + 1):
            if j - a >= 0 and k - b >= 0:
                dp[i + 1][j][k] = min(dp[i][j - a][k - b] + c, dp[i][j][k])
            else:
                dp[i + 1][j][k] = dp[i][j][k]
ans = float('inf')
for x in range(1, min(A // Ma, B // Mb) + 1):
    a = Ma * x
    b = Mb * x
    ans = min(dp[N][a][b], ans)
if ans == float('inf'):
    ans = -1
print(ans)
