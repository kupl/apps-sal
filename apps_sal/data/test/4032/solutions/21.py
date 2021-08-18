from collections import deque
import re
import math
import decimal
import bisect


def read():
    return input().strip()


def iread():
    return int(input().strip())


def viread():
    return list(map(int, input().strip().split()))


n, k = viread()
d = deque(viread())
solved = 0
while len(d) != 0 and (d[0] <= k or d[-1] <= k):
    if d[0] <= k:
        d.popleft()
        solved += 1
    elif d[-1] <= k:
        d.pop()
        solved += 1
print(solved)
