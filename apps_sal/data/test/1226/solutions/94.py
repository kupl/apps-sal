(n, a, b) = map(int, input().split())
mod = 10 ** 9 + 7


def cmb(n, r):
    (p, q) = (1, 1)
    for i in range(r):
        p = p * (n - i) % mod
        q = q * (i + 1) % mod
    return p * pow(q, mod - 2, mod) % mod


ALL = pow(2, n, mod) - 1
print((ALL - cmb(n, a) - cmb(n, b)) % mod)
