n,m,k = map(int,input().split())
mod = 10**9+7

def make_array_for_comb(N, mod=10**9+7):
    fact = [1,1]
    fact_inv = [1,1]
    inv = [0,1]
    for i in range(2, N+1):
        fact.append((fact[-1]*i) % mod)
        inv.append((-inv[mod%i] * (mod//i)) % mod)
        fact_inv.append((fact_inv[-1]*inv[i]) % mod)
    return fact, fact_inv

def comb(n, r, mod=10**9+7):
  if (r < 0) or (n < r):
      return 0
  r = min(r, n - r)
  return fact[n] * fact_inv[r] * fact_inv[n-r] % mod

fact, fact_inv = make_array_for_comb(n*m,mod)

l = comb(n*m-2,k-2,mod)
ans = 0
for a in range(1,n+1):
  ans += a*m*(a-1)*m
  ans -= a*m*(n-a)*m
ans %= mod

for b in range(1,m+1):
  ans += b*n*(b-1)*n
  ans -= b*n*(m-b)*n
ans %= mod

print(ans*l%mod)
