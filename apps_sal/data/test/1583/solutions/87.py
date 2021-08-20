import math
(a, b, x) = list(map(int, input().split()))
d = a * a * b
if x * 2 > d:
    x = d - x
    xx = 2 * x / (a * a * a)
    theta = math.atan(xx)
    print(theta * 180 / math.pi)
else:
    xx = 2 * x / (a * b * b)
    theta = math.atan(xx)
    print(90 - theta * 180 / math.pi)
