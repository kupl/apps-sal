def main():
    (n, m, k) = map(int, input().split())
    f = [1]
    p = 998244353
    for i in range(1, n):
        f.append(f[-1] * i % p)
    ans = 0

    def nCk(n, k):
        return f[n] * pow(f[n - k], p - 2, p) * pow(f[k], p - 2, p) % p
    for i in range(k + 1):
        ans += m * nCk(n - 1, i) * pow(m - 1, n - 1 - i, p) % p
    print(ans % p)


def __starting_point():
    main()


__starting_point()
