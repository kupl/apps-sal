def main():
    N = int(input())
    mod = 10 ** 9 + 7
    a = list(map(int, input().split()))
    ans = 0
    s = 0
    for i in range(1, N):
        s += a[i]
    for i in range(1, N):
        ans += a[i - 1] * s % mod
        s -= a[i]
    print(ans % mod)


def __starting_point():
    main()


__starting_point()
