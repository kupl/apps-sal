import numpy as np
import numba
from numba import njit, b1, i4, i8, f8

@njit((i8,i8,i8[:],i8[:]), cache=True)
def main(H,N,A,B):
  INF = 1<<30
  dp = np.full(H+1,INF,np.int64)
  dp[0] = 0
  for i in range(N):
    for h in range(A[i],H):
      dp[h] = min(dp[h],dp[h-A[i]]+B[i])
    dp[H] = min(dp[H],min(dp[H-A[i]:H]+B[i]))
  ans = dp[-1]
  return ans

H, N = map(int, input().split())
A = np.zeros(N,np.int64)
B = np.zeros(N,np.int64)
for i in range(N):
  A[i],B[i] = map(int, input().split())
print(main(H,N,A,B))
