from math import sin, cos, tan
PI = 3.141592653589793238463
[w, h, a] = [int(i) for i in input().split()]
if h > w:
    h, w = w, h
if a > 90:
    a = 180 - a
if a == 0:
    print(w * h)
else:
    b = (a * PI) / 180
    w = w / 2.0
    h = h / 2.0
    if tan(b / 2) >= h / w:
        print(4 * h * h / sin(b))
    else:
        ans = 4 * w * h
        m = -1 / tan(b)
        c = w * sin(b) + w * cos(b) / tan(b)
        ans = ans - (h - m * w - c) * (w - (h - c) / m)
        m = tan(b)
        c = h * cos(b) + h * sin(b) * tan(b)
        ans = ans - (h + m * w - c) * ((h - c) / m + w)
        print(ans)
