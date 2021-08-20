import math
import sys
import itertools
from decimal import *


def main():
    (k, a, b) = list(map(int, input().split()))
    mx = max(a, b)
    mn = min(a, b)
    r1 = mx % k
    r2 = mn % k
    d1 = mx // k
    d2 = mn // k
    if d2 == 0 and r1 != 0 or (d1 == 0 and r2 != 0):
        print(-1)
        return
    print(d1 + d2)


def __starting_point():
    main()


__starting_point()
