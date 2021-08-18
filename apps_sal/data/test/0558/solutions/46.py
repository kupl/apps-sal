n, m, k = map(int, input().split())


def cmb(n, r, mod):
    if (r < 0) or (n < r):
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % mod


mod = 998244353
N = 3 * 10**5
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]

for i in range(2, N + 1):
    fact.append((fact[-1] * i) % mod)
    inv.append((-inv[mod % i] * (mod // i)) % mod)
    factinv.append((factinv[-1] * inv[-1]) % mod)

ans = 0
for i in range(min(n, k + 1)):
    ans = (ans + cmb(n - 1, i, mod) * m * pow(m - 1, n - i - 1, mod)) % mod
print(ans)
