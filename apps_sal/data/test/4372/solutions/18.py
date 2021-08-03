import os

from math import gcd
from functools import reduce


def f(arr):
    max_a = max(arr)
    diffs = []
    for a in arr:
        diffs.append(max_a - a)

    z = reduce(gcd, diffs)
    y = 0
    for diff in diffs:
        y += int(diff / z)

    return f"{y} {z}"


if os.environ.get('DEBUG', False):
    print(f"{f([3, 12, 6])} = 5 3")
    print(f"{f([2, 9])} = 1 7")
    print(f"{f([2, 1000000000, 4, 6, 8, 4, 2])} = 2999999987 2")
    print(f"{f([13, 52, 0, 13, 26, 52])} = 12 13")
else:
    input()
    arr = list(map(int, input().split()))
    print(f(arr))
