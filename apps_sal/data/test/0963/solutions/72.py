N, K = list(map(int, input().split()))
A = []
for i in range(K):
  l, r = list(map(int, input().split()))
  A.append((l, r))
M = 998244353
dp = [0 for i in range(N+1)]
sumdp = [0 for i in range(N+1)]
dp[1] = 1
sumdp[1] = 1
for i in range(2, N+1):
  tmp = 0
  for l, r in A:
    l, r = i-r, i-l
    if r <= 0:
      continue
    l = max(1, l)
    tmp += (sumdp[r] - sumdp[l-1])
    tmp %= M
  dp[i] = tmp
  sumdp[i] = (sumdp[i-1] + dp[i])%M
print((dp[N]))

