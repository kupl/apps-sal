a, b, x, y = map(int, input().split())

if a == b:
    print(x)
elif a < b:
    if (b - a) * y + x < ((b - a) * 2 + 1) * x:
        print((b - a) * y + x)
    else:
        print(((b - a) * 2 + 1) * x)
else:
    if ((a - b) * 2 - 1) * x < (a - b - 1) * y + x:
        print(((a - b) * 2 - 1) * x)
    else:
        print((a - b - 1) * y + x)
