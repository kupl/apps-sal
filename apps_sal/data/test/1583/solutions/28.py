import math as m
a, b, x = map(int, input().split())
x /= a
P = m.acos(-1.0)
if x > a * b / 2: print(m.atan2((a * b - x) * 2, a * a) * 180 / P)
else: print(m.atan2(b * b, x * 2) * 180 / P)
