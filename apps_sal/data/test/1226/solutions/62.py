def main():
    (n, a, b) = map(int, input().split())
    mod = 10 ** 9 + 7

    def modpow(x, n, mod):
        res = 1
        while n:
            if n % 2:
                res *= x % mod
            x *= x % mod
            n >>= 1
        return res

    def cmb(n, r):
        nume = 1
        for i in range(n - r + 1, n + 1):
            nume = nume * i % mod
        deno = 1
        for j in range(1, r + 1):
            deno = deno * j % mod
        d = modpow(deno, mod - 2, mod)
        return nume * d
    all_cmb = pow(2, n, mod) - 1
    bad_a = cmb(n, a)
    bad_b = cmb(n, b)
    print((all_cmb - bad_a - bad_b) % mod)


def __starting_point():
    main()


__starting_point()
