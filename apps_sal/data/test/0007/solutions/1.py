n, m = map(int, input().split())


def calc(n):
    return (n + 1) * n // 2


if n <= m:
    print(n)
else:
    ans = m
    l = 0
    r = n - m
    while l < r - 1:
        mid = (l + r) // 2
        if calc(mid) >= n - m:
            r = mid
        else:
            l = mid

    if calc(l) >= n - m:
        r = l
    ans += r
    print(ans)
