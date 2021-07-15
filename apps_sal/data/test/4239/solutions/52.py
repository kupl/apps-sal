n = int(input())

dp = [1000000 for _ in range(n+1)]
dp[0] = 0

for i in range(0,n):
  if i+1 <= n:
    dp[i+1] = min(dp[i+1], dp[i] + 1)
  for j in range(1,7):
    a = 6**j
    if i+a <= n:
      dp[i+a] = min(dp[i+a], dp[i] + 1)
  for k in range(1,6):
    a = 9**k
    if i+a <= n:
      dp[i+a] = min(dp[i+a], dp[i] + 1)

print(dp[n])
