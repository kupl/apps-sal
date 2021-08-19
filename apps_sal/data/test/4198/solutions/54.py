(a, b, x) = map(int, input().split())
if a + b > x:
    print(0)
else:
    (l, r) = (0, 10 ** 9 + 1)
    while r - l > 1:
        mid = (l + r) // 2
        keta = len(str(mid))
        n = a * mid + b * keta
        if n > x:
            r = mid
        else:
            l = mid
    print(l)
