def dst1(x1, x2, y1, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def dst2(x1, x2, y1, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5


def getx(y):
    return (-b * y - c) / a


def gety(x):
    return (-a * x - c) / b


a, b, c = map(int, input().split())
x1, y1, x2, y2 = map(int, input().split())


def sign(a):
    if a > 0:
        return 1
    elif a == 0:
        return 0
    else:
        return -1


if a == 0 or b == 0:
    print(dst1(x1, x2, y1, y2))
else:
    s1 = dst1(x1, x2, y1, y2)

    p1x = x1
    p1y = gety(p1x)
    p3y = y1
    p3x = getx(p3y)

    p2x = x2
    p2y = gety(p2x)
    p4y = y2
    p4x = getx(p4y)

    s = 0
    s += dst1(x1, p1x, y1, p1y)
    s += dst2(p1x, p2x, p1y, p2y)
    s += dst1(p2x, x2, p2y, y2)
    s2 = s

    s = 0
    s += dst1(x1, p3x, y1, p3y)
    s += dst2(p3x, p2x, p3y, p2y)
    s += dst1(p2x, x2, p2y, y2)
    s3 = s

    s = 0
    s += dst1(x1, p1x, y1, p1y)
    s += dst2(p1x, p4x, p1y, p4y)
    s += dst1(p4x, x2, p4y, y2)
    s4 = s

    s = 0
    s += dst1(x1, p3x, y1, p3y)
    s += dst2(p3x, p4x, p3y, p4y)
    s += dst1(p4x, x2, p4y, y2)
    s5 = s

    print(min(s1, s2, s3, s4, s5))
