a, b, c, d = input().split()
a = int(a)
b = int(b)
c = int(c)
d = int(d)
if c < a < d:
    if b > d:
        print((d - a))
    else:
        print((b - a))
if a <= c:
    if b < c:
        print((0))
    elif c <= b <= d:
        print((b - c))
    else:
        print((d - c))
if a >= d:
    print((0))
