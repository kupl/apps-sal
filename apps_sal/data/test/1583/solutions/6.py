import math


def f(d):
    theta = d * math.pi / 180
    if a * math.tan(theta) <= b:
        return a * a * b - a * a * a * math.tan(theta) / 2
    else:
        return a * b * b / (2 * math.tan(theta))


a, b, x = map(int, input().split())
l, r = 0.0, 90.0
for i in range(1000):
    m = (l + r) / 2
    if f(m) <= x:
        r = m
    else:
        l = m
print('{0:.10f}'.format(l))
