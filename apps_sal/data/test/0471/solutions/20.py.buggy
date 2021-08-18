from math import *

[n, a] = [int(x) for x in input().split()]

if n == 1:
    print(0)
    return

points = [int(x) for x in input().split()]
points.sort()

dis1 = abs(points[n - 2] - points[0])
dis2 = abs(points[n - 1] - points[1])

to0 = abs(a - points[0])
to1 = abs(a - points[1])
ton = abs(a - points[n - 1])
ton2 = abs(a - points[n - 2])

print(min(to0 + dis1, to1 + dis2, ton + dis2, ton2 + dis1))
