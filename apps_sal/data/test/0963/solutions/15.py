N , K = map(int,input().split())
mod = 998244353
L = [0]*K
R = [0]*K
for i in range(K):
  L[i] , R[i] = map(int,input().split())
L.sort()
R.sort()
dp = [0]*(N+1)
sdp = [0]*(N+1)
dp[1] = 1
sdp[1] = 1
for i in range(1,N):
  tdp = 0
  for j in range(K):
    if i - L[j] + 1 >= 0 :
      s1 = sdp[i - L[j] + 1]
    else:
      s1 = 0
    if i - R[j] >= 0:
      s2 = sdp[i - R[j]]
    else:
      s2 = 0
    tdp += s1 - s2
  dp[i+1] = tdp%mod
  sdp[i+1] = (sdp[i] + dp[i+1])%mod
print(dp[N]%mod)  
