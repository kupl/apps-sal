def g(a, b, n, x, mod=10 ** 9 + 7):
    if a == 1:
        return (x + b * n) % mod
    z = pow(a, n, mod)
    inv = pow(a - 1 + mod, mod - 2, mod)
    return (z * x + b * (z - 1 + mod) * inv) % mod


print(g(*[int(x) for x in input().split()]))
