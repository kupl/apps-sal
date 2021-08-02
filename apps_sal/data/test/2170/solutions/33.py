n, m = map(int, input().split())
mod = 10**9 + 7

fact = [1, 1]
finv = [1, 1]
inv = [0, 1]

for i in range(2, max(n, m) + 5):
    fact.append((fact[-1] * i) % mod)
    inv.append((inv[mod % i] * (mod - mod // i)) % mod)
    finv.append((finv[-1] * inv[-1]) % mod)


def nCr(n, r, mod):
    if r > n:
        return 0
    else:
        return fact[n] * finv[r] * finv[n - r] % mod


def nPr(n, r, mod):
    if r > n:
        return 0
    else:
        return fact[n] * finv[n - r] % mod


ans = 0
for i in range(n + 1):
    now = nCr(n, i, mod)
    now *= nPr(m - i, n - i, mod)
    now %= mod
    if i % 2:
        now = -now
    ans += now
    ans % mod
ans *= nPr(m, n, mod)
ans %= mod
print(ans)
