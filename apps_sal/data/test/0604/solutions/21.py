import bisect
import collections
from functools import cmp_to_key

import sys


def getIntList():
    return list(map(int, input().split()))


n, = getIntList()

z = getIntList()

res = set()
for x in z:
    if x != 0:
        res.add(x)

print(len(res))
