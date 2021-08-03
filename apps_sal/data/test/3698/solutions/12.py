def main():
    s, k = input(), int(input())
    n = len(s)
    if k < 2:
        print((1, n - 1)[k])
        return
    tais = [n - i - 1 for i, c in enumerate(s) if c == '1']
    tlen, cache, res = len(tais), {}, 0

    def c(n, m):
        if n < m * 2:
            m = n - m
        if 0 < m:
            if (n, m) not in cache:
                cache[n, m] = (c(n - 1, m - 1) + c(n - 1, m)) % 1000000007
            return cache[n, m]
        return not m

    for m in range(n, 0, -1):
        x, t = m, k
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
            res += sum(c(t, m - i) for i, t in enumerate(tais)) + (m <= tlen)
    print(res % 1000000007)


def __starting_point():
    from sys import setrecursionlimit

    setrecursionlimit(1050)
    main()


__starting_point()
