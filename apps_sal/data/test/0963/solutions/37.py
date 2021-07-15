N,K = list(map(int,input().split()))
mod = 998244353

dp = [0] * (N+1)
dpSum = [0] * (N+1)
R = list()
L = list()

for i in range(K):
  l,r = list(map(int,input().split()))
  R.append(r)
  L.append(l)

dp[1] = 1
dpSum[1] = 1

for i in range(2,N+1,1):
  for j in range(K):
    li = i - R[j]
    ri = i - L[j]
    if ri <= 0:
      continue
    li = max(li,1)
    dp[i] += dpSum[ri] % mod - dpSum[li-1] % mod
  dpSum[i] = (dpSum[i-1] + dp[i]) % mod

ans = dp[N] % mod
print(ans)

