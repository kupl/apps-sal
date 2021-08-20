(r1, c1, r2, c2) = map(int, input().split())
mod = 10 ** 9 + 7
n = [1] * (r2 + c2 + 3)
for i in range(r2 + c2 + 2):
    n[i + 1] = n[i] * (i + 1) % mod


def g(a, b):
    (x, y, z) = (n[a + b], n[a], n[b])
    return x * pow(y, mod - 2, mod) % mod * pow(z, mod - 2, mod) % mod


print((g(r2 + 1, c2 + 1) - g(r2 + 1, c1) - g(r1, c2 + 1) + g(r1, c1)) % mod)
