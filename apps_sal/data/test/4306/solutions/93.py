a, b, c, d = (int(x) for x in input().split())

if a <= c <= b:
    if d <= b:
        print(d - c)
    else:
        print(b - c)
elif c <= a:
    if b <= d:
        print(b - a)
    elif a <= d <= b:
        print(d - a)
    else:
        print(0)
else:
    print(0)
