def main():
    n = int(input())
    a = list(map(int, input().split()))
    if n == 1:
        print(a[0])
        return
    mod = 998244353
    for i in range(1, n):
        a[i] += a[i - 1]
    ans = 0
    for i in range(n - 2):
        m = n - 1 - (i + 2)
        ans = (ans + pow(2, m, mod) * a[i] * (m + 5)) % mod
    print((ans + a[-2] + a[-2] + a[-1]) % mod)


def __starting_point():
    main()


__starting_point()
