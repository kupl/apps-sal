import sys
readline = sys.stdin.readline

N,M = map(int,readline().split())
INF = 10 ** 10
dp = [INF] * (2 ** N)
dp[0] = 0

for i in range(M):
  a,b = map(int,readline().split())
  c = list(map(int,readline().split()))
  key = 0
  for j in range(len(c)):
    key += (1 << (c[j] - 1))
  for j in range(len(dp)):
    if dp[j] == INF:
      continue
    if j | key == j:
      continue
    dp[j | key] = min(dp[j | key], dp[j] + a)

if dp[-1] == INF:
  print(-1)
else:
  print(dp[-1])
