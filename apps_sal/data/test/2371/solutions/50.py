N, Z, W = map(int, input().split())
A = list(map(int, input().split()))
if N == 1:
  print(abs(A[0]-W))
  return

dp = [[0, 0] for i in range(N)]
dp[-1][0] = abs(A[-1]- W)
dp[-1][1] = - 1
dp[-2][0] = dp[-2][1] = dp1min = abs(A[-2] - A[-1])
dp0max = max(dp1min, dp[-1][0])

for i in range(N-3, -1, -1):
  ai = A[i]
  diff = abs(ai - A[-1])
  dp[i][0] = min(diff, dp1min)
  dp[i][1] = max(diff, dp0max)
  dp0max = max(dp0max, dp[i][0])
  dp1min = min(dp1min, dp[i][1])

print(dp0max)
