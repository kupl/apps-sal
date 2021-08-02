import sys


def __starting_point():
    cin = sys.stdin

    n = int(next(cin))
    ax, ay = list(map(int, next(cin).split()))
    bx, by = list(map(int, next(cin).split()))
    cx, cy = list(map(int, next(cin).split()))

#   if cx == ax or cy == ay or cx-cy==ax-ay or cx+cy==ax+ay:
#       print('YES')
#       return
    if (ax - bx) * (ax - cx) > 0 and (ay - by) * (ay - cy) > 0:
        print('YES')
    else:
        print('NO')


__starting_point()
