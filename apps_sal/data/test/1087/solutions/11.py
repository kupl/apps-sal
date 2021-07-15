n, k = map(int, input().split())
A = list(map(int, input().split()))
M = 40
C = [[0]*2 for _ in range(M+1)]
for a in A:
  for i in range(M+1):
    C[i][a>>i & 1] += 1
dp = [[0]*2 for _ in range(M+1)]
dp[M][1] = -float("inf")
for i in range(M-1, -1, -1):
  j = k>>i & 1
  dp[i][0] = dp[i+1][0]*2 + C[i][j^1]
  dp[i][1] = dp[i+1][1]*2 + max(C[i])
  if j:
    dp[i][1] = max(dp[i][1], dp[i+1][0]*2 + C[i][1])
ans = max(dp[0])
print(ans)
