import sys
import collections
import math
import heapq
from operator import itemgetter


def getint():
    return int(input())


def getints():
    return [int(x) for x in input().split(' ')]


n = getint()
points = [tuple(getints()) for _ in range(n)]
result = total = 0
slopes = collections.defaultdict(set)
for i in range(n - 1):
    for j in range(i + 1, n):
        (x1, y1, x2, y2) = (points[i][0], points[i][1], points[j][0], points[j][1])
        (a, b) = (y1 - y2, x1 - x2)
        d = math.gcd(a, b)
        (a, b) = (a // d, b // d)
        if a < 0 or (a == 0 and b < 0):
            (a, b) = (-a, -b)
        c = a * x1 - b * y1
        slope = (a, b)
        if c not in slopes[slope]:
            total += 1
            slopes[slope].add(c)
            result += total - len(slopes[slope])
print(str(result))
