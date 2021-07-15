n=int(input())
a=[int(input())for _ in range(n)]
dp=[2]*(n+1)
from bisect import bisect_left,bisect_right
for i in a:
  dp[bisect_left(dp,-i+1)]=-i
print(dp.index(2))
