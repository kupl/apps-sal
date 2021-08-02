a, b, x, y = [int(i) for i in input().split()]

if a == b:
    print(x)
elif a < b:
    if 2 * x > y:
        print(((b - a) * y + x))
    else:
        print((2 * (b - a) * x + x))
else:
    if 2 * x > y:
        print(((a - b - 1) * y + x))
    else:
        print((2 * (a - b) * x - x))
