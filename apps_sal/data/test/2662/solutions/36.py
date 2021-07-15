from bisect import bisect
N = int(input())
dp = [1]*N
for _ in range(N):
  a=-int(input())
  n=bisect(dp,a)
  dp[n]=a
print(sum(1 for i in dp if i <= 0))
