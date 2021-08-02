def main():
    n = int(input())
    A = list(map(int, input().split()))

    mod = 10**9 + 7
    ans = 0

    for k in range(60):
        x, y = 0, 0
        for a in A:
            x += 1 & a >> k
        tmp = x * (n - x) % mod
        tmp *= pow(2, k, mod)
        ans += tmp
        ans %= mod
    print(ans)


def __starting_point():
    main()


__starting_point()
