a, b, c, d = list(map(int, input().split()))
if d <= a:
    print((0))
    return
if a <= c <= b:
    if b >= d:
        print((d - c))
        return
    else:
        print((b - c))
        return
elif c < a:
    if b >= d:
        print((d - a))
        return
    else:
        print((b - a))
        return
else:
    print((0))

