import math
(a, b, x) = map(int, input().split())
if x >= 1 / 2 * a * a * b:
    y = 2 * (b - x / (a * a))
    print(math.degrees(math.atan2(y, a)))
else:
    y = 2 * x / (a * b)
    print(math.degrees(math.atan2(b, y)))
