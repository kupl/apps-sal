(n, a, b) = map(int, input().split())
mod = 10 ** 9 + 7


def comb(n, m, mod=10 ** 9 + 7):
    numerator = 1
    denominator = 1
    for i in range(1, m + 1):
        numerator = numerator * (n - i + 1) % mod
        denominator = denominator * i % mod
    d_inv = pow(denominator, mod - 2, mod)
    return numerator * d_inv % mod


cmb_n_a = comb(n, a)
cmb_n_b = comb(n, b)
print((pow(2, n, mod) - 1 - cmb_n_a - cmb_n_b) % mod)
