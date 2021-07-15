import sys
readline = sys.stdin.readline

N,M = map(int,readline().split())
keys = [None] * M
for i in range(M):
  cost,b = map(int,readline().split())
  bit = 0
  target = list(map(int,readline().split()))
  for t in target:
    bit += (1 << (t - 1))
  keys[i] = (cost, bit)
    
# 全ての鍵の組み合わせでDP
INF = 10 ** 8 + 1
dp = [INF for i in range(2 ** N)]
dp[0] = 0
for key in keys:
  cost, bit = key
  for j in range(len(dp) - 1, -1, -1):
    if dp[j] == INF:
      continue
    if dp[j | bit] > dp[j] + cost:
      dp[j | bit] = dp[j] + cost

if dp[-1] == INF:
  print(-1)
else:
  print(dp[-1])
