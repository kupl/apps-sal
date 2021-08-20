def f(n, r, mod=10 ** 9 + 7):
    n += r
    assert n >= r >= 0

    def ex_euclid(x, y):
        (a, b) = (1, 0)
        while y != 0:
            (a, b) = (b, a - x // y * b)
            (x, y) = (y, x % y)
        return a
    p = q = 1
    for i in range(n - r + 1, n + 1):
        p *= i
        p %= mod
    for i in range(2, r + 1):
        q *= i
        q %= mod
    p *= ex_euclid(q, mod)
    p %= mod
    return p


(a, b, c, d) = map(int, input().split())
mod = 10 ** 9 + 7
print((f(c + 1, d + 1) + mod - f(a, d + 1) + mod - f(c + 1, b) + f(a, b)) % mod)
