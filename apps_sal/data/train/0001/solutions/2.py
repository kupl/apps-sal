q = int(input())
for i in range(q):
    (x, y, k) = list(map(int, input().split()))
    if x > y:
        (x, y) = (y, x)
    m = y
    d = y
    if (y - x) % 2 == 1:
        d -= 1
    if k < m:
        print(-1)
        continue
    r = k - m
    if r % 2 != 0:
        r -= 1
        if d != m:
            d += 1
        else:
            d -= 1
    d += r
    print(d)
