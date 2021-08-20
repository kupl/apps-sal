(a, b, c, x, y) = map(int, input().split())
if a + b > 2 * c:
    if x > y:
        if a > 2 * c:
            print(y * 2 * c + (x - y) * c * 2)
        else:
            print(y * 2 * c + (x - y) * a)
    elif b > 2 * c:
        print(x * 2 * c + (y - x) * c * 2)
    else:
        print(x * 2 * c + (y - x) * b)
else:
    print(x * a + y * b)
