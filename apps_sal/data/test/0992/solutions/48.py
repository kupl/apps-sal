import sys
input = sys.stdin.readline
import numpy as np

MOD = 998244353
n, s = map(int, input().split())
A = list(map(int, input().split()))
ans = 0
dp = np.zeros(s+1, dtype=np.int64)
dp[0] = 1
for a in A:
  t = dp.copy() * 2
  t[a:] += dp[:-a]
  t %= MOD
  dp = t
ans = dp[s]
print(ans)
