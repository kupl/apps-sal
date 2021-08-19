import math
(a, b, x) = list(map(int, input().split()))
x = x / a
if a * b / 2 < x:
    print(math.degrees(math.atan(2 * (a * b - x) / a ** 2)))
else:
    print(math.degrees(math.atan(b ** 2 / (2 * x))))
