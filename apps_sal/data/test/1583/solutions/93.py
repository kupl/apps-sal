import math
(a, b, x) = list(map(int, input().split()))
if x * 2 <= a * a * b:
    print(math.degrees(math.atan(a * b * b / (2 * x))))
else:
    print(math.degrees(math.atan((a * a * b - x) * 2 / a ** 3)))
