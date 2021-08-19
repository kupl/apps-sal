from math import fabs
EPS = 10 ** (-6)


def equal(a, b):
    return fabs(a - b) < EPS


def dist_sq(ax, ay, bx, by):
    return (ax - bx) * (ax - bx) + (ay - by) * (ay - by)


def triangle_area(ax, ay, bx, by, cx, cy):
    return ax * (by - cy) + bx * (cy - ay) + cx * (ay - by)


def main():
    (ax, ay, bx, by, cx, cy) = (int(x) for x in input().split())
    if equal(dist_sq(ax, ay, bx, by), dist_sq(bx, by, cx, cy)) and (not equal(triangle_area(ax, ay, bx, by, cx, cy), 0.0)):
        print('Yes')
    else:
        print('No')


def __starting_point():
    main()


__starting_point()
