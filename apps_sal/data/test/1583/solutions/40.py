import math
(a, b, x) = map(int, input().split())
if x == a ** 2 * b:
    print(0)
elif 2 * x <= a ** 2 * b:
    print(math.degrees(math.atan(b ** 2 * a / (2 * x))))
else:
    print(90 - math.degrees(math.atan(a ** 3 / (2 * (a ** 2 * b - x)))))
