def gcd(a, b):
    if a == 0:
        return (b, 0, 1)
    (g, x1, y1) = gcd(b % a, a)
    y = x1
    x = y1 - b // a * x1
    return (g, x, y)


def comp(da, db, t, a, b):
    ra = a + da * t
    rb = b + db * t
    return ra + rb


def solve():
    (x, y, p, q) = list(map(int, input().split()))
    if p == q:
        if x == y:
            print(0)
        else:
            print(-1)
        return
    if p == 0:
        if x == 0:
            print(0)
        else:
            print(-1)
        return
    r = x * q - y * p
    (g, a, b) = gcd(p - q, p)
    if r % g != 0:
        print(-1)
        return
    a *= r // g
    b *= r // g
    da = p
    db = q - p
    minT = -10 ** 18
    minT = max(minT, (-a + (da - 1)) // da)
    minT = max(minT, (-b + (db - 1)) // db)
    t = minT
    rr = comp(da, db, t, a, b)
    print(rr)


def main():
    t = int(input())
    for i in range(t):
        solve()


def __starting_point():
    main()


__starting_point()
