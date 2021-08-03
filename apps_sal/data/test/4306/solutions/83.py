a, b, c, d = map(int, input().split())
if b <= c or d <= a:
    print(0)
elif a <= c:
    if b <= d:
        print(b - c)
    else:
        print(d - c)
else:
    if b <= d:
        print(b - a)
    else:
        print(d - a)
