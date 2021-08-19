from math import atan
from math import pi
t = []


def f(x, y):
    if y == 0:
        if x > 0:
            return 0
        else:
            return pi
    if x == 0:
        if y > 0:
            return pi / 2
        else:
            return 3 * pi / 2
    if x > 0 and y > 0:
        return atan(y / x)
    if x < 0 and y < 0:
        return pi + atan(y / x)
    if x > 0 and y < 0:
        return 2 * pi + atan(y / x)
    if x < 0 and y > 0:
        return pi + atan(y / x)


def g(x, y):
    return 180 * f(x, y) / pi


for i in range(int(input())):
    (x, y) = list(map(int, input().split(' ')))
    t.append(g(x, y))
t.sort()
m = t[-1] - t[0]
for i in range(1, len(t)):
    m = min(m, 360 - (t[i] - t[i - 1]))
print(m)
