from collections import defaultdict as dd
from itertools import combinations
import math
import heapq


def nn():
    return int(input())


def li():
    return list(input())


def mi():
    return list(map(int, input().split()))


def lm():
    return list(map(int, input().split()))


n = nn()

points = []

for i in range(n):
    points.append(lm())


slopedict = dd(set)
lines = 0

for p1, p2 in combinations(points, 2):
    x1, y1 = p1
    x2, y2 = p2

    g = math.gcd(y2 - y1, x2 - x1)
    if y2 - y1 < 0:
        sign = -1

    elif y2 - y1 == 0:
        if x2 - x1 < 0:
            sign = -1
        else:

            sign = 1

    else:
        sign = 1
    slope = (sign * (y2 - y1) // g, sign * (x2 - x1) // g)

    if not slope[1] == 0:
        ceptn = slope[1] * y1 - slope[0] * x1
        ceptd = slope[1]

        if ceptn < 0:
            sign = -1

        elif ceptn == 0:
            if ceptd < 0:
                sign = -1
            else:

                sign = 1

        else:
            sign = 1

        g = math.gcd(ceptn, ceptd)
        cept = (sign * ceptn / g, sign * ceptd / g)
    else:
        cept = x1

    if not cept in slopedict[slope]:
        slopedict[slope].add(cept)
        lines += 1

total = 0


for slope in slopedict:

    total = total + (lines - len(slopedict[slope])) * len(slopedict[slope])


print(total // 2)

pos = math.gcd(-4, 2)
neg = math.gcd(4, -2)
# print(pos,neg)

# print(-4//pos,2//pos)

# print(4//neg,-2//neg)
