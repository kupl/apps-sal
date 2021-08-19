import functools
import math
import sys


def cmp(x, y):
    if x < y:
        return -1
    elif x > y:
        return 1
    else:
        return 0


print(''.join(sorted([s.rstrip() for s in sys.stdin.readlines()[1:]], key=functools.cmp_to_key(lambda x, y: cmp(x + y, y + x)))))
