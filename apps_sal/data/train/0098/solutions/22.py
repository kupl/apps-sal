q = int(input())
for i in range(q):
    (c, m, x) = map(int, input().split())
    if min(c, m) <= x:
        print(min(c, m))
    else:
        l = -1
        r = min(c, m) + 1
        while l + 1 < r:
            mid = (l + r) // 2
            if c - mid + m - mid + x >= mid:
                l = mid
            else:
                r = mid
        if l == -1:
            l = 0
        print(l)
