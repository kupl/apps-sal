import collections
from functools import cmp_to_key

import sys


def getIntList():
    return list(map(int, input().split()))


n, K = getIntList()

z = getIntList()
z.sort()


res = 0
last = -1
lastc = 0
for x in z:
    if x == last:
        lastc += 1
    elif last + K >= x:
        last = x
        lastc = 1
    else:
        res += lastc
        last = x
        lastc = 1

res += lastc

print(res)
