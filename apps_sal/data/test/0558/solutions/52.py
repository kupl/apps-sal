def main():
    n, m, k = list(map(int, input().split()))
    mod = 998244353

    def cmb(n, r, mod):
        if (r < 0 or r > n):
            return 0
        r = min(r, n - r)
        return g1[n] * g2[r] * g2[n - r] % mod

    N = 10**6
    g1 = [1, 1]
    g2 = [1, 1]
    inverse = [0, 1]

    for i in range(2, N + 1):
        g1.append((g1[-1] * i) % mod)
        inverse.append((-inverse[mod % i] * (mod // i)) % mod)
        g2.append((g2[-1] * inverse[-1]) % mod)

    s = 0
    for i in range(k + 1):
        s += cmb(n - 1, i, mod) * m * pow(m - 1, n - 1 - i, mod) % mod
    print((s % mod))


def __starting_point():
    main()


__starting_point()
