(n, m) = map(int, input().split())
mod = 10 ** 9 + 7
fact = [1] * (m + 1)
inv = [1] * (m + 1)
for i in range(2, m + 1):
    fact[i] = i * fact[i - 1] % mod
inv[-1] = pow(fact[-1], mod - 2, mod)
for i in range(m, 1, -1):
    inv[i - 1] = inv[i] * i % mod


def comb(x, y):
    return fact[x] * inv[y] % mod * inv[x - y] % mod if x >= y >= 0 else 0


def p(x, y):
    return fact[x] * inv[x - y] % mod if x >= y >= 0 else 0


ans = p(m, n) ** 2 % mod
a = -1
for i in range(1, n + 1):
    ans = (ans + a * (p(m, i) * comb(n, i) * p(m - i, n - i) ** 2 % mod)) % mod
    a *= -1
print(ans)
