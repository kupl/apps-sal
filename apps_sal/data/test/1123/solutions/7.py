def pow(a, n, mod):
    ret = 1
    pw = a
    while n > 0:
        if n & 1 == 1:
            ret *= pw
            ret %= mod
        n >>= 1
        pw *= pw
        pw %= mod
    return ret


def main():
    MOD = 10 ** 9 + 7
    N, K = list(map(int, input().split(' ')))
    n_gcds = [0 for _ in range(K + 1)]
    for g in range(K, 0, -1):
        v = pow(K // g, N, MOD)
        gg = g
        while gg + g <= K:
            gg += g
            v -= n_gcds[gg]
            v %= MOD
        n_gcds[g] = v
    ans = 0
    for g, n in enumerate(n_gcds):
        ans += g * n
        ans %= MOD
    print(ans)


def __starting_point():
    main()


__starting_point()
