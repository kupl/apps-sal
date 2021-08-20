import sys
import numpy as np


def IS():
    return sys.stdin.readline().rstrip()


def II():
    return int(IS())


def MII():
    return list(map(int, IS().split()))


def MIIZ():
    return list(map(lambda x: x - 1, MII()))


def main():
    (h, w, m) = MII()
    bombs = [MIIZ() for _ in range(m)]
    a = [0] * h
    b = [0] * w
    for (y, x) in bombs:
        a[y] += 1
        b[x] += 1
    maxa = max(a)
    maxb = max(b)
    sumv = maxa + maxb
    c = a.count(maxa) * b.count(maxb) - sum((a[y] + b[x] == sumv for (y, x) in bombs))
    print(sumv - (c <= 0))


def __starting_point():
    main()


__starting_point()
