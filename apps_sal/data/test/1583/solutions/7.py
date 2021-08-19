import math
(a, b, x) = [int(i) for i in input().split()]
if a ** 2 * b / 2 <= x:
    y = 2 * x / a ** 2 - b
    tntheta = (b - y) / a
else:
    y = a - 2 * x / (a * b)
    tntheta = b / (a - y)
print(math.degrees(math.atan(tntheta)))
