N,M = map(int,input().split())
E = [list(map(int,input().split())) for m in range(M)]
dp = (N+1)*[float("inf")]
dp[1] = 0

for n in range(N):
  for a,b,c in E:
    dp[b] = min(dp[b],dp[a]-c)

x = dp[N]

for a,b,c in E:
  dp[b] = min(dp[b],dp[a]-c)

if x!=dp[N]:
  print("inf")
else:
  print(-x)
