
import sys
import math
import os.path


def log(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def ni():
    return list(map(int, input().split(" ")))


def nio(offset):
    return [int(x) + offset for x in input().split(" ")]


def nia():
    return list(map(int, input().split()))


CMAX = 1000000000

n, = ni()
s = nia()
c = nia()


l1 = {}
l2 = {}

for j in range(1, n):
    for i in range(j):
        if (s[i] < s[j]):
            l1[j] = min(l1.get(j, CMAX), c[i])
            l2[i] = min(l2.get(i, CMAX), c[j])


res = CMAX

for i in range(n):
    res = min(res, l1.get(i, CMAX) + l2.get(i, CMAX) + c[i])

if (res < CMAX):
    print(res)
else:
    print(-1)
