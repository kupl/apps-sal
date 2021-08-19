import math


def ans():
    (r, x1, y1, x2, y2) = [int(i) for i in input().split()]
    d = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
    if d % (2 * r) == 0:
        print(int(d / (2 * r)))
    else:
        print(int(d / (2 * r)) + 1)
    return


ans()
