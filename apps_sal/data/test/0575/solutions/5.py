import sys


def __starting_point():
    cin = sys.stdin

    n = int(next(cin))
    ax, ay = list(map(int, next(cin).split()))
    bx, by = list(map(int, next(cin).split()))
    cx, cy = list(map(int, next(cin).split()))

    if (ax - bx) * (ax - cx) > 0 and (ay - by) * (ay - cy) > 0:
        print('YES')
    else:
        print('NO')


__starting_point()
