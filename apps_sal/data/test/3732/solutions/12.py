(x, y, m) = map(int, input().split())
if x < y:
    (x, y) = (y, x)
if x >= m:
    print(0)
elif x > 0:
    s = 0
    if y < 0:
        s = -y // x + 1
        y += x * s
    while x < m:
        (x, y) = (x + y, x)
        s += 1
    print(s)
elif x < m:
    print(-1)
else:
    print(0)
