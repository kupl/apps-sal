import math
(a, b, x) = map(int, input().split())
x_s = a * a * b - x
if x <= x_s:
    print(math.degrees(math.atan(a * b * b / (2 * x))))
else:
    print(math.degrees(math.atan(2 * x_s / (a * a * a))))
