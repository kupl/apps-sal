from collections import defaultdict
import sys
import os
import math


def __starting_point():
    s, x1, x2 = list(map(int, input().split()))
    t1, t2 = list(map(int, input().split()))
    p, d = list(map(int, input().split()))
    if t1 >= t2:
        print(abs(x2 - x1) * t2)
        return

    if x2 > x1:
        if d == 1:
            if p <= x1:
                t = t1 * (x2 - p)
            else:
                t = t1 * (s + s - p + x2)
        else:
            t = t1 * (p + x2)
    else:
        if d == -1:
            if p >= x1:
                t = t1 * (p - x2)
            else:
                t = t1 * (s + s - x2 + p)
        else:
            t = t1 * (s - p + s - x2)
    print(min(t, abs(x2 - x1) * t2))


__starting_point()
