def combs_mod(n,k,mod):
  #nC0からnCkまで
  inv = [1]*(k+1)
  for i in range(1,k+1):
    inv[i] = pow(i,mod-2,mod)
  ans = [1]*(k+1)
  for i in range(1,k+1):
    ans[i] = ans[i-1]*(n+1-i)*inv[i]%mod
  return ans

def solve():
  ans = 0
  mod = 998244353
  N, M, K = map(int, input().split())
  top = min(K,N-1)
  combs = combs_mod(N-1,top,mod)
  for k in range(top+1):
    ans += M*combs[k]*pow(M-1,N-1-k,mod)
    ans %= mod
  return ans
print(solve())
