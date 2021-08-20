def cmb(n, r, mod):
    if r < 0 or n < r:
        return 0
    r = min(r, n - r)
    return fact[n] * factinv[r] * factinv[n - r] % mod


mod = 10 ** 9 + 7
N = 10 ** 6
fact = [1, 1]
factinv = [1, 1]
inv = [0, 1]
for i in range(2, N + 1):
    fact.append(fact[-1] * i % mod)
    inv.append(-inv[mod % i] * (mod // i) % mod)
    factinv.append(factinv[-1] * inv[-1] % mod)
(n, k) = map(int, input().split())
ans = 0
for i in range(0, min(n, k + 1)):
    ans = (ans + cmb(n, i, mod) * cmb(n - 1, i, mod)) % mod
print(ans)
