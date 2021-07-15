import  numpy as np
N, W, *L = map(int, open(0).read().split())
M = 3*(N-1)+1
dp = np.zeros((M,N+1),np.int64)
for w,v in zip(*[iter(L)]*2):
  w -= L[0]
  dp[w:,1:] = np.maximum(dp[w:,1:], dp[:M-w,:N]+v)

ans = 0
for i in range(N+1):
  m = i*L[0]
  if m>W:
    continue
  m = min(W-m,M-1)
  ans = max(ans, dp[m,i])
print(ans)
