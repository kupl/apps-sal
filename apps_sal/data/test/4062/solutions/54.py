a, b, c, d = map(int, input().split())
if a >= 0 and b >= 0:
    if d >= 0:
        print(b * d)
    else:
        print(a * d)
elif a < 0 and b >= 0:
    if c >= 0 and d >= 0:
        print(b * d)
    elif c < 0 and d >= 0:
        if abs(a) * abs(c) >= b * d:
            print(abs(a) * abs(c))
        else:
            print(b * d)
    elif c < 0 and d < 0:
        print(a * c)
elif a < 0 and b < 0:
    if c >= 0 and d >= 0:
        print(b * c)
    elif c < 0:
        print(a * c)
