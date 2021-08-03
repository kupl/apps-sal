h, w, a, b = list(map(int, input().split()))

mod = 10**9 + 7
fact = [1, 1]
finv = [1, 1]
inv = [0, 1]

for i in range(2, h + w + 5):
    fact.append((fact[-1] * i) % mod)
    inv.append((inv[mod % i] * (mod - mod // i)) % mod)
    finv.append((finv[-1] * inv[-1]) % mod)


def nCr(n, r, mod):
    if r > n:
        return 0
    else:
        return fact[n] * finv[r] * finv[n - r] % mod


ans = 0

for i in range(100000):
    x = h - a - i
    y = b + 1 + i

    if 0 >= x or y > w:
        break

    ans += nCr(h + w - x - y, h - x, mod) * nCr(x + y - 2, x - 1, mod) % mod
    ans %= mod
print(ans)
