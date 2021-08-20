def ext_gcd(a, b):

    def _ext_gcd(a, b):
        xs = [1, 0]
        ys = [0, 1]
        sign = 1
        while b != 0:
            (q, r) = (a // b, a % b)
            (a, b) = (b, r)
            (xtmp, ytmp) = (xs[1], ys[1])
            (xs[1], ys[1]) = (q * xs[1] + xs[0], q * ys[1] + ys[0])
            (xs[0], ys[0]) = (xtmp, ytmp)
            sign = -sign
        return (a, (sign * xs[0], -sign * ys[0]))
    if a < b:
        (d, (y, x)) = _ext_gcd(b, a)
        return (d, (x, y))
    return _ext_gcd(a, b)


def __starting_point():
    (X, Y) = map(int, input().split())
    if (2 * Y - X) % 3 != 0 or (2 * X - Y) % 3 != 0:
        print(0)
        return
    (a, b) = ((2 * Y - X) // 3, (2 * X - Y) // 3)
    if a < 0 or b < 0:
        print(0)
        return
    n = 1
    k = 1
    l = 1
    mod = 10 ** 9 + 7
    for i in range(2, a + b + 1):
        n = n * i % mod
        if i <= a:
            k = k * i % mod
        if i <= b:
            l = l * i % mod
    (_, (k, _)) = ext_gcd(k, mod)
    (_, (l, _)) = ext_gcd(l, mod)
    print(n * k * l % mod)


__starting_point()
