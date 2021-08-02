MOD = 10**9 + 7


def main():
    n = int(input())
    c = list(map(int, input().split()))
    c.sort()
    ans = 0
    for i in range(n):
        tmp = pow(2, i, MOD)
        if i < n - 1:
            tmp *= pow(2, n - i - 1, MOD) + pow(2, n - i - 2, MOD) * (n - i - 1)
        else:
            tmp *= pow(2, n - i - 1, MOD)
        tmp %= MOD
        ans += c[i] * tmp
    print(ans * pow(2, n, MOD) % MOD)


def __starting_point():
    main()


__starting_point()
