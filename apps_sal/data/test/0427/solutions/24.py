s = input()
c1, c2, x, y = list(map(int, s.split()))

l = 0
r = int(1e18)

while r - l > 1:
    m = (l + r) // 2

    d1 = m // x
    d2 = m // y
    b = m // (x * y)

    k1 = d2 - b
    k2 = d1 - b

    rr = m - d1 - d2 + b

    r1 = max(0, c1 - k1)
    r2 = max(0, c2 - k2)

    if rr >= r1 + r2:
        r = m
    else:
        l = m

print(r)
