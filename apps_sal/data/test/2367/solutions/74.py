mod = 10 ** 9 + 7
fact = [1]
inv = [1]
for i in range(200000):
    fact.append(fact[i] * (i + 1) % mod)
    inv.append(pow(fact[i + 1], mod - 2, mod))


def ncr(n, r):
    if n < 0 or r < 0 or n - r < 0:
        return 0
    return fact[n] * inv[r] * inv[n - r] % mod


h, w, a, b = list(map(int, input().split()))
ans = ncr(h + w - 2, h - 1)
for i in range(min(a, b)):
    ans -= ncr(h - a + b - 1, h - a + i) * ncr(w - b + a - 1, w - b + i)
print((ans % mod))
