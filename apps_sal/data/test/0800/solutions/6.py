from math import *
n = int(input())
pts = [list(map(float, input().split())) for _ in range(n)]
a = sorted([atan2(y, x) for x, y in pts])
d = [a[i] - a[i - 1] for i in range(1, len(a))]
d.append(2 * pi + a[0] - a[-1])
print(degrees(2 * pi - max(d)))
