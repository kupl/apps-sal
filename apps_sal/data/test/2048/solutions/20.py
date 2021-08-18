
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


l1 = [CMAX for _ in range(n)]
l2 = [CMAX for _ in range(n)]

for j in range(1, n):
    for i in range(j):
        if (s[i] < s[j]):
            l1[j] = min(l1[j], c[i])
            l2[i] = min(l2[i], c[j])


res = CMAX

for i in range(n):
    res = min(res, l1[i] + l2[i] + c[i])

if (res < CMAX):
    print(res)
else:
    print(-1)
