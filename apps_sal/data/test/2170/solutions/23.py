def prepare(n, MOD):
    f = 1
    fn = [1] * (n + 1)
    for m in range(1, n + 1):
        f *= m
        f %= MOD
        fn[m] = f
    inv = pow(f, MOD - 2, MOD)
    invs = [1] * (n + 1)
    invs[n] = inv
    for m in range(n, 1, -1):
        inv *= m
        inv %= MOD
        invs[m - 1] = inv
    return (fn, invs)


def main():
    (n, m) = map(int, input().split())
    MOD = 10 ** 9 + 7
    (fn, invs) = prepare(m, MOD)
    ans = 0
    for i in range(n + 1):
        x = fn[m - i] * invs[m - n] % MOD
        x = x * fn[n] * invs[i] * invs[n - i] % MOD
        x *= (-1) ** i
        ans += x
    ans = ans * fn[m] * invs[m - n] % MOD
    print(ans)


def __starting_point():
    main()


__starting_point()
