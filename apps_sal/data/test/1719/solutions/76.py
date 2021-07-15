import numpy as np

N = int(input())
mod = 10**9+7

dp = np.zeros([N+1,4,4,4],dtype=int)
dp[0,-1,-1,-1] = 1

for i in range(N):
  for c1 in range(4):
    for c2 in range(4):
      for c3 in range(4):
        if not dp[i,c1,c2,c3]:continue
        for a in range(4):
          if c1 == 0 and c3 == 1 and a == 2:continue
          if c1 == 0 and c2 == 1 and a == 2:continue
          if c2 == 0 and c3 == 1 and a == 2:continue
          if c2 == 0 and c3 == 2 and a == 1:continue
          if c2 == 1 and c3 == 0 and a == 2:continue
          dp[i+1,c2,c3,a] += dp[i,c1,c2,c3]
          dp[i+1,c2,c3,a] %= mod

print(dp[-1].sum()%mod)
