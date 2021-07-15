from math import hypot, sqrt

R, x1, y1, x2, y2 = list(map(int, input().split()))

if hypot(x1 - x2, y1 - y2) > R:
    print(x1, y1, R)

elif (x1, y1) == (x2, y2):
    print(x1 + R / 2, y1, R / 2)

else:
    A = y2 - y1
    B = x1 - x2
    C = -x1 * (y2 - y1) + y1 * (x2 - x1)

    if A != 0:
        A1 = A ** 2 + B ** 2
        B1 = 2 * (B * C + A * B * x1 - A ** 2 * y1)
        C1 = A ** 2 * (x1 ** 2 + y1 ** 2 - R ** 2) + C ** 2 + 2 * A * C * x1

        D = B1 ** 2 - 4 * A1 * C1

        Y1 = (-B1 + sqrt(D)) / (2 * A1)
        Y2 = (-B1 - sqrt(D)) / (2 * A1)

        X1 = (-B * Y1 - C) / A
        X2 = (-B * Y2 - C) / A

        h1 = hypot(x2 - X1, y2 - Y1)
        h2 = hypot(x2 - X2, y2 - Y2)

        if h1 > h2:
            print((x2 + X1) / 2, (y2 + Y1) / 2, h1 / 2)

        else:
            print((x2 + X2) / 2, (y2 + Y2) / 2, h2 / 2)


    elif B != 0:
        A1 = A ** 2 + B ** 2
        B1 = 2 * (A * C + A * B * y1 - B ** 2 * x1)
        C1 = B ** 2 * (x1 ** 2 + y1 ** 2 - R ** 2) + C ** 2 + 2 * B * C * y1

        D = B1 ** 2 - 4 * A1 * C1

        X1 = (-B1 + sqrt(D)) / (2 * A1)
        X2 = (-B1 - sqrt(D)) / (2 * A1)

        Y1 = (-A * X1 - C) / B
        Y2 = (-A * X2 - C) / B

        h1 = hypot(x2 - X1, y2 - Y1)
        h2 = hypot(x2 - X2, y2 - Y2)

        if h1 > h2:
            print((x2 + X1) / 2, (y2 + Y1) / 2, h1 / 2)

        else:
            print((x2 + X2) / 2, (y2 + Y2) / 2, h2 / 2)

    else:
        exit(100500)

