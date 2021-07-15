import math

R, x1, y1, x2, y2 = list(map(int, input().split()))

v = [x1 - x2, y1 - y2]

if v != [0, 0]:
    lv = math.hypot(v[0], v[1])
    if lv <= R:
        sf = ((lv + R) / lv) / 2
        vs = [v[0] * sf, v[1] * sf]

        r = math.hypot(vs[0] - x2, vs[1] - y2)

        print(x2 + vs[0], y2 + vs[1], (lv + R) / 2)
    else:
        print(x1, y1, R)
else:
    print(x1 + R / 2, y1, R / 2)

