import math
import sys
from collections import defaultdict


def nt():
    return list(map(int, input().split()))


def main():
    (n, r) = nt()
    projects = [tuple(nt()) for _ in range(n)]
    positive = [t for t in projects if t[1] > 0]
    negative = [t for t in projects if t[1] <= 0]
    ok = True
    for p in sorted(positive):
        if p[0] <= r:
            r += p[1]
        else:
            ok = False
            break
    if ok:
        for p in sorted(negative, key=lambda x: -x[0] - x[1]):
            if p[0] <= r:
                r += p[1]
                if r < 0:
                    ok = False
                    break
            else:
                ok = False
                break
    print('YES' if ok else 'NO')


def __starting_point():
    main()


__starting_point()
