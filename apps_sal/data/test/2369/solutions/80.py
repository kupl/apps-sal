N, K = map(int, input().split())
A = list(map(int, input().split()))
mod = 10**9 + 7
A.sort(reverse=True)
"""
kaijou = [1 for _ in range(N+1)]
for k in range(1, N):
  kaijou[k+1] = kaijou[k]*(k+1)%mod



b = mod-2
blis = []
c = 0
while b >0:
  if b & 1 == 1:
    blis.append(c)
  c += 1
  b >>= 1

def modinv(a):
  if a == 1:
    return 1
  else:
    res = 1
    li = []
    for _ in range(c):
      li.append(a%mod)
      a = a*a%mod
    for item in blis:
      res = res *li[item] %mod
    return res
"""
fact = [1, 1]  # fact[n] = (n! mod p)
factinv = [1, 1]  # factinv[n] = ((n!)^(-1) mod p)
inv = [0, 1]  # factinv 計算用

for i in range(2, N + 1):
    fact.append((fact[-1] * i) % mod)
    inv.append((-inv[mod % i] * (mod // i)) % mod)
    factinv.append((factinv[-1] * inv[-1]) % mod)


def combination(n, k):
    #foo = kaijou[n]*modinv(kaijou[k]*kaijou[n-k]%mod)%mod
    foo = fact[n] * factinv[k] * factinv[n - k] % mod
    return foo


ans = 0

for k in range(N - K + 1):
    ans += A[k] * combination(N - k - 1, K - 1)
    ans %= mod

for k in range(N - K + 1):
    ans -= A[-k - 1] * combination(N - k - 1, K - 1)
    ans %= mod

print(ans)
