def main():
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))
    a.sort()
    mod = 10 ** 9 + 7
    fac = [1 for _ in range(n + 1)]
    inv = [1 for _ in range(n + 1)]
    for i in range(1, n + 1):
        fac[i] = fac[i - 1] * i
        fac[i] %= mod
        inv[i] = inv[i - 1] * pow(i, -1, mod)
        inv[i] %= mod

    def comb(a, b, mod):
        return (fac[a] * inv[b] * inv[a - b]) % mod

    ans = 0
    for i in range(k - 1, n):
        nck = comb(i, k - 1, mod)
        ans += nck * a[i]
        ans -= nck * a[n - i - 1]
        ans %= mod

    print(ans)


def __starting_point():
    main()


__starting_point()
