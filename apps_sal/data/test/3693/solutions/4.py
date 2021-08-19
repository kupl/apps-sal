def cp(a, b):
    return a[0] * b[1] - a[1] * b[0]


def sub(b, a):
    return (b[0] - a[0], b[1] - a[1])


def ccw(a, b, c):
    r = cp(sub(b, a), sub(c, a))
    if r == 0:
        return 0
    elif r > 0:
        return 1
    else:
        return -1


def sortpts(pts):
    return pts if ccw(pts[0], pts[1], pts[2]) > 0 else list(reversed(pts))


def readpts():
    ip = list(map(int, input().split()))
    return sortpts([(ip[i], ip[i + 1]) for i in range(0, 8, 2)])


def segi(a1, a2, b1, b2):
    c1 = ccw(a1, a2, b1)
    c2 = ccw(a1, a2, b2)
    return c1 != c2


def segib(a1, a2, b1, b2):
    return segi(a1, a2, b1, b2) and segi(b1, b2, a1, a2)


def checkpts(pts1, pts2):
    for p1 in pts1:
        aa = True
        for i in range(4):
            j = (i + 1) % 4
            if ccw(pts2[i], pts2[j], p1) < 0:
                aa = False
        if aa:
            return True
    return False


def checkpts2(pts1, pts2):
    for i in range(4):
        for j in range(4):
            if segib(pts1[i], pts1[(i + 1) % 4], pts2[j], pts2[(j + 1) % 4]):
                return True
    return False


pts1 = readpts()
pts2 = readpts()
# print(pts1)
# print(pts2)
print('YES' if checkpts(pts1, pts2) or checkpts(pts2, pts1) or checkpts2(pts1, pts2) else 'NO')
