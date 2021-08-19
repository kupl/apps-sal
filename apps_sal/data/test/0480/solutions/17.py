import sys
from decimal import *


def check(t, w, s, p1, d1, p2, d2):
    if t * w >= 2 * s:
        return True


def main():
    (s, a, b) = list(map(int, sys.stdin.readline().split()))
    (w, v) = list(map(int, sys.stdin.readline().split()))
    (p1, d) = list(map(int, sys.stdin.readline().split()))
    r = abs(a - b) * v
    if v <= w:
        print(r)
        return
    if p1 <= a:
        t_ = 0
        if d == -1 and p1 != a:
            t_ = p1 * w
            a = a - t_ / v
            p1 = 0
            d = 1
        t1 = (a - p1) * v * w / (v + w)
        x1 = a - t1 / v
        t1 += t_
    else:
        t_ = 0
        if d == 1:
            t_ = (s - p1) * w
            a = a + t_ / v
            p1 = s
            d = -1
        t1 = (p1 - a) * v * w / (v + w)
        x1 = a + t1 / v
        t1 += t_
    if d == 1:
        if x1 <= b:
            t2 = (b - x1) * w
        else:
            t2 = (2 * s - x1 - b) * w
    elif x1 >= b:
        t2 = (x1 - b) * w
    else:
        t2 = (x1 + b) * w
    t3 = t1 + t2
    t3i = int(t3)
    if t3i < t3 - 1e-06:
        t3i += 1
    print(min(r, t3i))


main()
