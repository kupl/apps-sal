def ext_euc(a, b):
    if b == 0:
        return (1, 0, a)
    (y, x, v) = ext_euc(b, a % b)
    y -= a // b * x
    return (x, y, v)


def mod_inv(a, mod):
    (x, _, _) = ext_euc(a, mod)
    return x % mod


def comb(n, k, mod):
    if k >= n // 2:
        return comb(n, n - k, mod)
    ret = 1
    for i in range(k):
        ret *= n - i
        ret *= mod_inv(k - i, mod)
        ret %= mod
    return ret


def main():
    MOD = 10 ** 9 + 7
    (N, M, K) = list(map(int, input().split(' ')))
    ans = comb(N * M - 2, K - 2, MOD)
    ans *= (N ** 2 * (M - 1) * M * (M + 1) + M ** 2 * (N - 1) * N * (N + 1)) // 6
    ans %= MOD
    print(ans)


def __starting_point():
    main()


__starting_point()
