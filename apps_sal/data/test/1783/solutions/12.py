def main():
    n, k = list(map(int, input().split()))
    a = list(map(int, input().split()))

    ans = 0

    for i in range(n):
        l = max(i - k + 1, 0)
        r = min(i, n - k)
        ans += a[i] * (r - l + 1)

    print("{:.12f}".format(ans / (n - k + 1)))


def __starting_point():
    main()


__starting_point()
