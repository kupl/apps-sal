from math import sin, sqrt, radians
(n, r) = map(int, input().split())
o = 360 / (n * 2)
a = o / 2
c = 180 - o - a
A = r * sin(radians(a)) / sin(radians(c))
O = r * sin(radians(o)) / sin(radians(c))
S = (A + O + r) / 2
area = 0.5 * A * r * sin(radians(o))
print(2 * n * area)
