from collections import *
N,W = map(int,input().split())
dp = defaultdict(int)
dp[0] = 0

for n in range(N):
  w1,v1 = map(int,input().split())
  for w2,v2 in dp.copy().items():
    if w1+w2<=W:
      dp[w1+w2] = max(dp[w1+w2],v1+v2)

print(max(dp.values()))
