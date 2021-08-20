A = list(map(int, input()))
while A[-1] == 0:
    A.pop()
n = len(A)
dp = [[0] * 2 for _ in range(n)]
dp[0][1] = 1
for (i, a) in enumerate(A[:-1]):
    if i < n - 1:
        dp[i + 1][0] = min(dp[i][0] + a, dp[i][1] + 10 - a)
        dp[i + 1][1] = min(dp[i][0] + a + 1, dp[i][1] + 9 - a)
ans = min(dp[-1][0] + A[-1], dp[-1][1] + 10 - A[-1])
print(ans)
