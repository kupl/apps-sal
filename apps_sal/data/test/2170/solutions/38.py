#二項係数、順列準備
MAX_NUM = 5* 10**5 + 1
MOD = 10**9+7

fac  = [0 for _ in range(MAX_NUM)]
finv = [0 for _ in range(MAX_NUM)]
inv  = [0 for _ in range(MAX_NUM)]

fac[0]  = fac[1] = 1
finv[0] = finv[1] = 1
inv[1] = 1

for i in range(2,MAX_NUM):
  fac[i] = fac[i-1] * i % MOD
  inv[i] = MOD - inv[MOD%i] * (MOD // i) % MOD
  finv[i] = finv[i-1] * inv[i] % MOD

def comb(n,k):
  if n < k:
    return 0
  if n < 0 or k < 0:
    return 0
  return fac[n] * (finv[k] * finv[n-k] % MOD) % MOD

def perm(n,k):
  if n < k:
    return 0
  if n < 0 or k < 0:
    return 0
  return fac[n] * finv[n-k] % MOD

#主計算
N, M = map(int,input().split())

ans = 0
for K in range(N+1):
  term = comb(N, K) * perm(M, K) 
  term *= perm(M - K, N - K)**2
  term %= MOD
  if K % 2 == 0:
    ans = (ans + term) % MOD
  else:
    ans = (ans - term) % MOD
    
print(ans)
