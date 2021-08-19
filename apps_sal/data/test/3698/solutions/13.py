def main():
    (s, k) = (input(), int(input()))
    n = len(s)
    if k < 2:
        print((1, n - 1)[k])
        return
    tais = [n - i - 1 for (i, c) in enumerate(s) if c == '1']
    (tlen, mod, res) = (len(tais), 1000000007, 0)
    (fac, ifac, f) = ([1], [1], 1)
    for i in range(1, n + 1):
        f = f * i % mod
        fac.append(f)
        x = v = 0
        y = u = 1
        (a, b) = (f, mod)
        while a:
            (q, r) = divmod(b, a)
            (a, b, x, y, u, v) = (r, a, u, v, x - u * q, y - v * q)
        ifac.append(x)

    def c(n, m):
        return fac[n] * ifac[m] * ifac[n - m] % mod if 0 <= m <= n else 0
    for m in range(n, 0, -1):
        (x, t) = (m, k)
        while x != 1:
            y = 0
            t -= 1
            while x:
                y += x & 1
                x //= 2
            x = y
        if t == 1:
            if len(tais) > m:
                del tais[m:]
            res += sum((c(t, m - i) for (i, t) in enumerate(tais))) + (m <= tlen)
    print(res % mod)


def __starting_point():
    main()


__starting_point()
