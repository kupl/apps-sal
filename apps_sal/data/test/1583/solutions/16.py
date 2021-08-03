import math
a, b, x = list(map(int, input().split()))

if x >= a * a * b / 2:
    print((math.degrees(math.atan((b - x / (a * a)) / (a / 2)))))
else:
    print((90 - math.degrees(math.atan(((2 * x) / (b * a)) / b))))
