a, b, c, d = map(int, input().split())

if (b <= c) | (d <= a):
    print(0)
else:
    if (a <= c) & (b <= d):
        print(b - c)
    elif (c <= a) & (d <= b):
        print(d - a)
    else:
        print(min(d - c, b - a))
