(a, b, x, y) = [int(x) for x in input().split()]
if 2 * x >= y:
    if b >= a:
        print(x + (b - a) * y)
    else:
        print(x + (a - b - 1) * y)
elif b >= a:
    print(2 * x * (b - a) + x)
else:
    print(2 * x * (a - b - 1) + x)
