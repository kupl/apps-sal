(a, b, x, y) = map(int, input().split())
if a == b:
    print(x)
elif a > b:
    if 2 * x > y:
        print(x + (a - b - 1) * y)
    else:
        print(2 * x * (a - b - 1) + x)
elif 2 * x > y:
    print((b - a) * y + x)
else:
    print(2 * (b - a) * x + x)
