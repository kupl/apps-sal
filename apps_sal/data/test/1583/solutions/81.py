# ----------------
# ここから
# ----------------

import sys
import math
from io import StringIO
import unittest


def yn(b):
    print(("Yes" if b == 1 else "No"))
    return


def resolve():
    readline = sys.stdin.readline

    a, b, x = list(map(int, readline().rstrip().split()))
    if x <= a * a * b / 2:
        l = x * 2 / b / a
        print((math.degrees(math.atan(b / l))))
        return
    l = (2 * x) / (a * a) - b
    print((math.degrees(math.atan((b - l) / a))))
    #arr=list(map(int, readline().rstrip().split()))
    # n=int(readline())
    # ss=readline().rstrip()
    # yn(1)

    return


if 'doTest' not in globals():
    resolve()
    return

# ----------------
# ここまで
# ----------------
