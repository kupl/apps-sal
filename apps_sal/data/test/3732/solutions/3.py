(x, y, m) = list(map(int, input().split()))
(x, y) = (min(x, y), max(x, y))
if y >= m:
    print(0)
elif y <= 0:
    print(-1)
else:
    c = 0
    if x <= 0:
        q = (-x + y - 1) // y
        c += q
        x += q * y
    while y < m:
        (x, y) = (y, x + y)
        c += 1
    print(c)
