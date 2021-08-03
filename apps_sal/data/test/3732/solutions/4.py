x, y, m = list(map(int, input().split()))
x, y = min(x, y), max(x, y)
if y >= m:
    print(0)
elif y <= 0:
    print(-1)
else:
    c = 0
    while y < m:
        q = (2 * y - x) // y
        c += q
        x, y = y, x + q * y
    print(c)
