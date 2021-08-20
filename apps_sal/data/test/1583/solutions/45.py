import math


def slv(n, m):
    return math.tan(n) * m * m / 2


(a, b, x) = map(int, input().split())
c = a * a / 2
ang = 0.5 * math.pi
sang = ang
if x > c * b:
    x = a * a * b - x
    for i in range(1000):
        if slv(ang, a) * a > x:
            ang -= sang / 2 ** (i + 1)
        else:
            ang += sang / 2 ** (i + 1)
    print(math.degrees(ang))
else:
    for i in range(1000):
        if slv(ang, b) * a > x:
            ang -= sang / 2 ** (i + 1)
        else:
            ang += sang / 2 ** (i + 1)
    print(math.degrees(math.pi / 2 - ang))
