import math
(a, b, x) = map(int, input().split())
r = 180 / math.pi
c = x / (a * b * 0.5)
if c <= a:
    print(math.atan(b / c) * r)
else:
    c = (a ** 2 * b - x) * 2 / a ** 2
    print(math.atan(c / a) * r)
