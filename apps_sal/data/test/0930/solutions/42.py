n, k = list(map(int, input().split()))
p = 10**9 + 7

fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]

for i in range(2, n + 1):
    fact.append((fact[-1] * i) % p)
    inv.append(-inv[p % i] * (p // i) % p)
    factinv.append(factinv[-1] * inv[-1] % p)

def cmb(n, r, p):
    if n < r:
        return 0
    else:
        r = min(r, n - r)
        return((fact[n] * factinv[r] * factinv[n - r]) % p)

res = []
for i in range(n):
    res.append((cmb(n, i, p) * cmb(n - 1, i, p)) % p)

if n > k:
    print((sum(res[:k + 1]) % p))
else:
    print((sum(res) % p))

