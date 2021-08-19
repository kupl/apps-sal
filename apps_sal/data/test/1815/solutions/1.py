from collections import defaultdict as dd
import math


def nn():
    return int(input())


def li():
    return list(input())


def mi():
    return list(map(int, input().split()))


def lm():
    return list(map(int, input().split()))


n = nn()
l = lm()
d = {}
mnum = 0
colors = 0
singlecolors = 0
maxstring = 0
maxhit = 0
for (i, num) in enumerate(l):
    if num in d:
        d[num] += 1
        if d[num] == mnum:
            maxhit += 1
        elif d[num] > mnum:
            mnum = max(mnum, d[num])
            maxhit = 1
        if d[num] == 2:
            singlecolors -= 1
    else:
        d[num] = 1
        singlecolors += 1
        if d[num] == mnum:
            maxhit += 1
        elif d[num] > mnum:
            mnum = max(mnum, d[num])
            maxhit = 1
        colors += 1
    if maxhit == 1 and i == (mnum - 1) * colors or (maxhit >= colors - 1 and singlecolors >= 1):
        maxstring = i + 1
print(maxstring)
