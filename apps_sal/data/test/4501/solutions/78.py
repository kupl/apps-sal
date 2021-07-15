n,a = map(int, input().split())
X = list(map(int, input().split()))
x = [i-a for i in X]
dp = [[0]*5201 for i in range(n+1)]
dp[0][2600] = 1 
for i,xi in enumerate(x):
  for k in range(99,5101):
    dp[i+1][k+xi] += dp[i][k] 
    dp[i+1][k] += dp[i][k]
ans = dp[n][2600] - 1
print(ans)
