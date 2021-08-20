(a, b) = map(int, input().split())
(c, d) = map(int, input().split())
l = 0
r = 10 ** 10
if a * d == b * c:
    print(0)
else:
    for i in range(10000):
        x = (l + r) / 2
        a1 = (a - x) * (d - x)
        a2 = (a + x) * (d + x)
        a3 = (a + x) * (d - x)
        a4 = (a - x) * (d + x)
        b1 = (b - x) * (c - x)
        b2 = (b + x) * (c + x)
        b3 = (b + x) * (c - x)
        b4 = (b - x) * (c + x)
        mna = min(a1, a2, a3, a4)
        mxa = max(a1, a2, a3, a4)
        mnb = min(b1, b2, b3, b4)
        mxb = max(b1, b2, b3, b4)
        if mxa >= mnb and mxb >= mna:
            r = x
        else:
            l = x
    print('%0.10f' % x)
