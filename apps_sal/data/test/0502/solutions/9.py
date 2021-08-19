(ax, ay, bx, by, cx, cy) = list(map(int, input().split()))


def r(x1, y1, x2, y2):
    return (x1 - x2) ** 2 + (y1 - y2) ** 2


def line(x3, y3, x1, y1, x2, y2):
    if (x3 - x1) * (y2 - y1) == (y3 - y1) * (x2 - x1):
        return True
    return False


if r(ax, ay, bx, by) == r(bx, by, cx, cy) and (not line(ax, ay, bx, by, cx, cy)):
    print('Yes')
else:
    print('No')
