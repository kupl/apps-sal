a, b, c = [int(i) for i in input().split()]
n = max(a, b, c) + 1
mod = 998244353
f = [0] * (n + 1)
f[0] = 1
for i in range(1, n + 1):
    f[i] = (f[i - 1] * i) % mod


def f_pow(a, k):
    if k == 0:
        return 1
    if k % 2 == 1:
        return f_pow(a, k - 1) * a % mod
    else:
        return f_pow(a * a % mod, k // 2) % mod


def C(n, k):
    d = f[k] * f[n - k] % mod
    return f[n] * f_pow(d, mod - 2) % mod


ans, cur = 1, 0

for i in range(min(a, b) + 1):
    cur += C(a, i) * C(b, i) * f[i]
    cur %= mod
ans, cur = (ans * cur) % mod, 0

for i in range(min(b, c) + 1):
    cur += C(b, i) * C(c, i) * f[i]
    cur %= mod
ans, cur = (ans * cur) % mod, 0

for i in range(min(a, c) + 1):
    cur += C(a, i) * C(c, i) * f[i]
    cur %= mod

print((ans * cur) % mod)
