s, x1, x2 = list(map(int, input().split()))
t1, t2 = list(map(int, input().split()))
p, d = list(map(int, input().split()))
if x1 > x2:
    x1 = s - x1
    x2 = s - x2
    d *= -1
    p = s - p


def dist(sx, fx, d, s):
    if d == -1:
        return sx + fx
    else:
        if fx >= sx:
            return fx - sx
        else:
            return 2 * s - abs(fx - sx)


if t1 > t2:
    print(t2 * (x2 - x1))
else:
    print(min(dist(p, x1, d, s) * t1 + (x2 - x1) * t1, (x2 - x1) * t2))
