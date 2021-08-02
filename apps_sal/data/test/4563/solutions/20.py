n = int(input())
pt, pa = 0, 0
for _ in range(n):
    t, a = tuple(map(int, input().split()))
    l = 0
    r = 10**18 + 1
    while (r - l) > 1:
        mid = (l + r) // 2
        if (t * mid >= pt and a * mid >= pa):
            r = mid
        else:
            l = mid
    pt, pa = t * r, a * r

print((pt + pa))
