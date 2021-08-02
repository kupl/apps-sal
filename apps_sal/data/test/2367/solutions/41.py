def combmod(n, r, p):
    if r < 0 or n < r:
        return 0
    return fact[n] * finv[r] * finv[n - r] % p


p = 10**9 + 7
N = 10**6
fact = [1, 1]
finv = [1, 1]
inv = [0, 1]

for i in range(2, N + 1):
    fact.append((fact[-1] * i) % p)
    inv.append((-inv[p % i] * (p // i)) % p)
    finv.append((finv[-1] * inv[-1]) % p)

h, w, a, b = (int(x) for x in input().split())
ans = 0
for j in range(b, w):
    ans += combmod(h - a - 1 + j, j, p) * combmod(a + w - 2 - j, w - 1 - j, p)
print((ans % p))
