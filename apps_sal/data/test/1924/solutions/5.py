(r1, c1, r2, c2) = list(map(int, input().split()))
mod = 10 ** 9 + 7
MAX_N = 3 * 10 ** 6
fact = [1]
fact_inv = [0] * (MAX_N + 4)
for i in range(MAX_N + 3):
    fact.append(fact[-1] * (i + 1) % mod)
fact_inv[-1] = pow(fact[-1], mod - 2, mod)
for i in range(MAX_N + 2, -1, -1):
    fact_inv[i] = fact_inv[i + 1] * (i + 1) % mod


def comb(n, k, mod):
    if n < k:
        return 0
    return fact[n] * fact_inv[k] % mod * fact_inv[n - k] % mod


ans = 0
ans += comb(c1 + r1, r1, mod)
ans %= mod
ans -= comb(c1 + r2 + 1, r2 + 1, mod)
ans %= mod
ans -= comb(c2 + r1 + 1, r1, mod)
ans %= mod
ans += comb(c2 + r2 + 2, r2 + 1, mod)
ans %= mod
print(ans)
