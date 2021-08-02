import sys
import math


def v():
    pt = [5, 0, 1, 2]
    N = 100000
    s = list(['0' if x == 'g' else '1' for x in list(sys.stdin.readline().strip())])
    n, x = len(s), int(''.join(s), 2)
    s = list(format(x << (N - n), '0100000b'))
    p = pt[n % 4]
    for _ in range(n // 4):
        p = (p << 4) + 5
    ss = list(format(p << (N - n), '010000b'))
    res = 0
    for _, a, b in zip(list(range(n)), s, ss):
        d = int(b) - int(a)
        res = res if d == 0 else res + d
    print(res)


def __starting_point(): v()


__starting_point()
