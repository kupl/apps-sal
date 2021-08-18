def siblings(initial, root):
    th = (initial[0] - root[0], initial[1] - root[1])
    return [(root[0] + th[0], root[1] + th[1]),
            (root[0] - th[1], root[1] + th[0]),
            (root[0] - th[0], root[1] - th[1]),
            (root[0] + th[1], root[1] - th[0])]


def dist(x, y):
    return (x[0] - y[0])**2 + (x[1] - y[1])**2


def isSquare(p1, p2, p3, p4):
    d2 = dist(p1, p2)
    d3 = dist(p1, p3)
    d4 = dist(p1, p4)

    u = {p1, p2, p3, p4}
    if (len(u) != 4):
        return 0

    if (d2 == d3 and 2 * d2 == d4):
        d = dist(p2, p4)
        return (d == dist(p3, p4) and d == d2)

    if (d3 == d4 and 2 * d3 == d2):
        d = dist(p2, p3)
        return (d == dist(p2, p4) and d == d3)

    if (d2 == d4 and 2 * d2 == d3):
        d = dist(p2, p3)
        return (d == dist(p3, p4) and d == d2)

    return False


def distOri(x, y, root):
    th1 = (y[0] - root[0], y[1] - root[1])
    th2 = (x[0] - root[0], x[1] - root[1])
    if th1[0] == th2[0] and th1[1] == th2[1]:
        return 0
    if (th2[0] == -th1[1] and th2[1] == th1[0]):
        return 1
    if (th2[0] == - th1[0] and th2[1] == -th1[1]):
        return 2
    if (th2[0] == th1[1] and th2[1] == -th1[0]):
        return 3


n = int(input())

for i in range(n):
    initial = []
    root = []

    _max = 1000
    for j in range(4):
        x, y, a, b = [int(k) for k in input().split()]
        initial.append((x, y))
        root.append((a, b))

    for x1 in siblings(initial[0], root[0]):
        for x2 in siblings(initial[1], root[1]):
            for x3 in siblings(initial[2], root[2]):
                for x4 in siblings(initial[3], root[3]):
                    if isSquare(x1, x2, x3, x4):
                        _max = min(_max,
                                   distOri(x1, initial[0], root[0]) + distOri(x2, initial[1], root[1]) +
                                   distOri(x3, initial[2], root[2]) + distOri(x4, initial[3], root[3]))
    if (_max == 1000):
        print(-1)
    else:
        print(_max)
