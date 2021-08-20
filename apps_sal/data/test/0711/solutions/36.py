from math import floor, sqrt
(mod1, mod2) = (10 ** 9 + 7, 998244353)
mod = mod1
(n, m) = map(int, input().split())
mod = 10 ** 9 + 7
fact = [1] * (n + 50 + 1)
inv = [1] * (n + 50 + 1)
for i in range(2, n + 50 + 1):
    fact[i] = i * fact[i - 1] % mod
inv[-1] = pow(fact[-1], mod - 2, mod)
for i in range(n + 50, 1, -1):
    inv[i - 1] = inv[i] * i % mod


def comb(x, y):
    return fact[x] * inv[y] % mod * inv[x - y] % mod if x >= y >= 0 else 0


ans = 1
for i in range(2, floor(sqrt(m)) + 1):
    if m % i:
        continue
    cnt = 0
    while m % i == 0:
        cnt += 1
        m //= i
    ans = ans * comb(n - 1 + cnt, cnt) % mod
if m != 1:
    ans = ans * comb(n, 1) % mod
print(ans)
