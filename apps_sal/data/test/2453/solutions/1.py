from copy import deepcopy
import itertools
from bisect import bisect_left
from bisect import bisect_right
import math
from collections import deque


def read():
    return int(input())


def readmap():
    return list(map(int, input().split()))


def readlist():
    return list(map(int, input().split()))


N = read()
LIST = []
left = 0
right = 1
for i in range(N):
    l, r = readmap()
    LIST.append((l, left))
    LIST.append((r, right))

LIST.sort()

cnt = [0] * (N + 1)

n = 1
x = LIST[0][0]
dir = left
for item in LIST[1:]:
    if item[1] == left:
        if dir == left:
            cnt[n] += item[0] - x
            n += 1
            x = item[0]
            dir = left
        else:
            cnt[n] += item[0] - x - 1
            n += 1
            x = item[0]
            dir = left
    else:
        if dir == left:
            cnt[n] += item[0] - x + 1
            n -= 1
            x = item[0]
            dir = right
        else:
            cnt[n] += item[0] - x
            n -= 1
            x = item[0]
            dir = right

print(" ".join(list(map(str, cnt[1:]))))
