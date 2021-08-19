(n, k, *a) = list(map(int, open(0).read().split()))
a.sort()
mod = 10 ** 9 + 7
fact = [1] * (n + 1)
for i in range(1, n + 1):
    fact[i] = fact[i - 1] * i % mod


def inv(x):
    return pow(x, mod - 2, mod)


def c(n, k):
    return fact[n] * inv(fact[n - k] * fact[k] % mod) % mod


ans = 0
for i in range(k - 1, n):
    ans += a[i] * c(i, k - 1) % mod
a = list(reversed(a))
for i in range(k - 1, n):
    ans -= a[i] * c(i, k - 1) % mod
print((ans + mod) % mod)
