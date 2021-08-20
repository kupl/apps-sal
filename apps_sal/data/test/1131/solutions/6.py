import sys


def solve():
    (a, b, w, x, c) = map(int, input().split())
    w -= x
    (small, large) = (0, int(1e+20))
    while small < large:
        avg = (small + large) // 2
        if works(avg, a, b, c, w, x):
            large = avg
        else:
            small = avg + 1
    return small


def works(val, a, b, c, w, x):
    cres = c - val
    amin = cres
    maxsubtract = a - amin
    if maxsubtract < 0:
        return False
    bsubtract = val - maxsubtract
    bres = b + maxsubtract * w - x * bsubtract
    return bres >= 0


if sys.hexversion == 50594544:
    sys.stdin = open('test.txt')
print(solve())
