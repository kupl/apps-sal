import sys
readline = sys.stdin.readline

N,M = list(map(int,readline().split()))

INF = 10 ** 9
dp = [INF] * (2 ** N)
dp[0] = 0
for i in range(M):
  a,b = list(map(int,readline().split()))
  C = list(map(int,readline().split()))
  key = 0
  for c in C:
    key += (1 << (c - 1))
  for j in range(len(dp) - 1, -1, -1):
    if dp[j] == INF:
      continue
    if dp[j | key] > dp[j] + a:
      dp[j | key] = dp[j] + a

if dp[-1] == INF:
  print((-1))
else:
  print((dp[-1]))

