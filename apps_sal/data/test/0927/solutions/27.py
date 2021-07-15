n, m = map(int, input().split())
D = [0, 2, 5, 5, 4, 5, 6, 3, 7, 6]
A = list(map(int, input().split()))
C = [(a, D[a]) for a in A]
C.sort(reverse=True)
dp = [-1]*(n+1)
dp[0] = 0
for i in range(1, n+1):
  for a, c in C:
    if i >= c and dp[i-c] >= 0:
      dp[i] = max(dp[i-c]+1, dp[i])
now = n
ans = ""
while now:
  for a, c in C:
    if now-c >= 0 and dp[now] == dp[now-c]+1:
      ans += str(a)
      now -= c
      break
print(ans)
