(a, b, x, y) = list(map(int, input().split()))
if 2 * x >= y:
    if a <= b:
        print(x + y * (b - a))
    else:
        print(x + y * (a - 1 - b))
elif a <= b:
    print(x + 2 * x * (b - a))
else:
    print(x + 2 * x * (a - 1 - b))
