import math
a, b, x = map(int, input().split())
V = a * a * b
if 2 * x <= V:
    print(90 - math.degrees(math.atan((2 * x) / (a * b * b))))
else:
    print(math.degrees(math.atan((2 * (a * a * b - x)) / (a * a * a))))
