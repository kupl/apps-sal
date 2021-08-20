(N, K) = map(int, input().split())
A = list(map(int, input().split()))
mod = 10 ** 9 + 7
A.sort(reverse=True)
'\nkaijou = [1 for _ in range(N+1)]\nfor k in range(1, N):\n  kaijou[k+1] = kaijou[k]*(k+1)%mod\n\n\n\nb = mod-2\nblis = []\nc = 0\nwhile b >0:\n  if b & 1 == 1:\n    blis.append(c)\n  c += 1\n  b >>= 1\n\ndef modinv(a):\n  if a == 1:\n    return 1\n  else:\n    res = 1\n    li = []\n    for _ in range(c):\n      li.append(a%mod)\n      a = a*a%mod\n    for item in blis:\n      res = res *li[item] %mod\n    return res\n'
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]
for i in range(2, N + 1):
    fact.append(fact[-1] * i % mod)
    inv.append(-inv[mod % i] * (mod // i) % mod)
    factinv.append(factinv[-1] * inv[-1] % mod)


def combination(n, k):
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
