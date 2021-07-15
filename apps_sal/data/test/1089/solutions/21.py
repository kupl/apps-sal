N, M ,K = map(int, input().split())
MOD = 10**9 + 7

def comb(n, r, mod=10**9+7):
  if n==0 and r==0:
    return 1
  else:
    a = b = 1
    A, B = n, r
    for i in range(r):
      a = a*A % mod
      b = b*B % mod
      A -= 1
      B -= 1
    return a * pow(b, mod-2, mod) % mod

ans = comb(N*M-2, K-2) * ((M*(N-1)*(N+1) + N*(M-1)*(M+1))*N*M//6)%MOD % MOD
print(ans)
