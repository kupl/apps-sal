def mod_combination(n, k, mod=10 ** 9 + 7):

    def extended_gcd(a, b):
        if b == 0:
            return (a, 1, 0)
        (d, x, y) = extended_gcd(b, a % b)
        return (d, y, x - a // b * y)
    (p, q) = (1, 1)
    for i in range(n - k + 1, n + 1):
        p = p * i % mod
    for i in range(2, k + 1):
        q = q * i % mod
    return p * (extended_gcd(q, mod)[1] % mod) % mod


mod = 10 ** 9 + 7
(r1, c1, r2, c2) = map(int, input().split())


def f(i, j):
    return mod_combination(i + j, i)


print((f(r2 + 1, c2 + 1) - f(r2 + 1, c1) - f(r1, c2 + 1) + f(r1, c1)) % mod)
