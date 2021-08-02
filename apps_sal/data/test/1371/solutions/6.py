mod = 10**9 + 7
fact = [1]
for i in range(1, 2001):
    fact.append(i * fact[-1] % mod)
inv = [pow(i, mod - 2, mod) for i in fact]


def ncr(n, r):
    return fact[n] * inv[r] * inv[n - r] % mod


s = int(input())
ans = 0
for i in range(1, s // 3 + 1):
    ans += ncr(s - 3 * i + i - 1, i - 1)
print((ans % mod))
