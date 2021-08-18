def solve():
    n, k = map(int, input().split())
    a = [0] + list(map(int, input().split()))
    for i in range(1, n + 1):
        a[i] = a[i - 1] + a[i]
    ans = 0.0
    for i in range(k, n + 1):
        ans += (a[i] - a[i - k]) / (n - k + 1)
    print(ans)


def __starting_point():
    solve()


__starting_point()
