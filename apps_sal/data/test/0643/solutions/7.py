def gcd(a, b):
    if (a == 0):
        return (b, 0, 1)

    (g, x, y) = gcd(b % a, a)
    return (g, y - (b // a) * x, x)


t = int(input())

for i in range(t):
    (x, y, p, q) = list(map(int, input().split()))
    val = p * y - q * x
    (g, a, b) = gcd(q, -p)

    if (val % g != 0):
        print(-1)
        continue

    a *= val // g
    b *= val // g

    da = abs(p // g)
    db = abs(q // g)

    if (a < 0):
        if (da == 0):
            print(-1)
            continue

        mul = (abs(a) + da - 1) // da
        a += mul * da
        b += mul * db

    if (b < 0):
        if (db == 0):
            print(-1)
            continue

        mul = (abs(b) + db - 1) // db
        a += mul * da
        b += mul * db

    if (a > b):
        if (da == db):
            print(-1)
            continue

        diff = a - b
        step = db - da
        mul = (diff + step - 1) // step
        a += mul * da
        b += mul * db

    mul = b // db
    if (da != 0):
        mul = min(mul, a // da)

    if (da != db):
        mul = min(mul, (b - a) // (db - da))

    print(b - db * mul)
