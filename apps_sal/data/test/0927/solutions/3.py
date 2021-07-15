n, m = map(int, input().split())
A = list(map(int, input().split()))

li = [2,5,5,4,5,6,3,7,6]

dp = [-1] * (n + 1)
dp[0] = 0

for i in range(n):
  for j in A:
    if i + li[j - 1] <= n:
      dp[i + li[j - 1]] = max(dp[i + li[j - 1]], dp[i] * 10 + j)
print(dp[-1])
