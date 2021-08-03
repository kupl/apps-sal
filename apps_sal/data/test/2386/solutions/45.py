def main():
    n = int(input())
    a = list(map(int, input().split()))
    l = -1 * max(a) - 2 * 10**5
    r = max(a) + 2 * 10**5

    def f(k):
        ans = 0
        for i in range(n):
            ans += abs(a[i] - 1 - i - k)
        return ans
    while l + 1 < r:
        if f(l) < f(r):
            r = (l + r) // 2
        else:
            l = (l + r) // 2
    print((min(f(l), f(r))))


def __starting_point():
    main()


__starting_point()
