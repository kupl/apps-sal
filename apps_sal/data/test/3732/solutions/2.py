(x, y, m) = list(map(int, input().split()))
if max(x, y) >= m:
    print(0)
elif x <= 0 and y <= 0:
    print(-1)
else:
    if x > y:
        (x, y) = (y, x)
    (ans, st) = (0, 0)
    add = 0
    if x <= 0:
        st = (0 - x + y - 1) // y
        x += y * st
    ans = st + (m - x + y - 1) // y
    while y < m:
        (x, y) = (y, x + y)
        add += 1
        ans = min(ans, add + st + (m - x + y - 1) // y)
    ans = min(ans, add + st)
    print(ans)
