from math import *
(n, r) = map(int, input().split())
x = 360 / n
a = x / 4 / 180 * pi
b = x * 3 / 4 / 180 * pi
x = tan(a)
y = tan(b)
S = r ** 2 * sin(a) * cos(a) / 2
S1 = r * sin(a) / tan(b) * r * sin(a) / 2
S2 = S - S1
print(S2 * 2 * n)
