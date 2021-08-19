import math
(a, b, x) = list(map(int, input().split()))
full = a * a * b
if x > full / 2:
    x = full - x
    tan_x = 2.0 * x / (a * a) / a
    print(math.atan(tan_x) / math.pi * 180.0)
else:
    tan_x = 2.0 * x / (a * b) / b
    print(90 - math.atan(tan_x) / math.pi * 180.0)
