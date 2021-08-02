n, k = map(int, input().split())
*a, = map(int, input().split())
l, r = 0, 10**9
while r - l > 1:
    m = (l + r) // 2
    t = 0
    for x in a:
        if x <= m:
            continue
        t += (x + m - 1) // m - 1
    if t <= k:
        r = m
    else:
        l = m
print(r)
