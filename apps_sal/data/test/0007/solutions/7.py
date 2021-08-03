import sys

n, m = list(map(int, input().split()))

if n <= m:
    print(n)
    return

else:
    l, r = m + 1, n
    base = m * (m - 1) // 2

    while l != r:
        mid = (l + r) // 2
        plus = n + base + (mid - m) * m
        minus = mid * (mid + 1) // 2
        if plus > minus:
            l = mid + 1
        else:
            r = mid
    print(l)
