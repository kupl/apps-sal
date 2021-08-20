import math
(a, b, x) = map(int, input().split())
v = a * a * b
if v / 2 >= x:
    print(math.degrees(math.atan(a * b * b / (2 * x))))
else:
    print(math.degrees(math.atan(2 * (v - x) / a ** 3)))
