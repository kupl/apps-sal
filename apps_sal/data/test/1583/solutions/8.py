import math
(a, b, x) = map(int, input().split())
if 0.5 * a ** 2 * b <= x:
    print(math.degrees(math.atan((2 * a ** 2 * b - 2 * x) / a ** 3)))
else:
    print(math.degrees(math.atan(a * b ** 2 / (x * 2))))
