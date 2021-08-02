a, b, c, x, y = map(int, input().split())

if a + b <= 2 * c:
    print(a * x + b * y)
else:
    if x <= y:
        if b <= 2 * c:
            print(2 * c * x + b * (y - x))
        else:
            print(2 * c * y)
    else:
        if a <= 2 * c:
            print(2 * c * y + (x - y) * a)
        else:
            print(2 * c * x)
