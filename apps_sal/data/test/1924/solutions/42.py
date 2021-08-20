(r, c, R, C) = [int(_) for _ in input().split()]
mod = 10 ** 9 + 7
f = [1] * (2 * 10 ** 6 + 10)
for i in range(1, 2 * 10 ** 6 + 10):
    f[i] = i * f[i - 1] % mod


def comb(x, y):
    return f[x] * pow(f[y], mod - 2, mod) * pow(f[x - y], mod - 2, mod)


print((comb(C + R + 2, R + 1) - comb(c + R + 1, R + 1) - comb(C + r + 1, r) + comb(c + r, r)) % mod)
