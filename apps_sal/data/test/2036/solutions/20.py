import sys
import heapq
import functools
import collections
import math
import random
from collections import Counter, defaultdict


def solve(h, w, x, y):
    console("----- solving ------")
    x, y = x - 1, y - 1

    for _ in range(h):
        for _ in range(w):
            print("{} {}".format(x + 1, y + 1))
            y = (y + 1) % w
        y = (y - 1) % w
        x = (x + 1) % h

    return


def console(*args):
    print('\033[36m', *args, '\033[0m', file=sys.stderr)
    return


h, w, x, y = list(map(int, input().split()))


solve(h, w, x, y)
