def mod_exp(x, y, p):
    res = 1
    x %= p
    while y:
        if y & 1:
            res = res * x % p
        y >>= 1
        x = x * x % p
    return res


def power(a, b, m):
    (x, y) = (1, a)
    while b:
        if b & 1:
            x = x * y % m
        y = y * y % m
        b //= 2
    return x


def mod_inverse(a, m):
    return power(a, m - 2, m)


def solve(a, b, n, x):
    m = 10 ** 9 + 7
    if a == 1:
        return (b * n * a + x) % m
    p = mod_exp(a, n, m)
    return (b * (p - 1) * mod_inverse(a - 1, m) + p * x) % m


(a, b, n, x) = list(map(int, input().split()))
print(solve(a, b, n, x))
