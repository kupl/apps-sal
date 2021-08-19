import math
(a, b, x) = [int(n) for n in input().split()]
v = a ** 2 * b / 2
if v == x:
    theta = math.atan(b / a)
elif v > x:
    theta = math.atan(a * b ** 2 / (2 * x))
elif v < x:
    theta = math.atan(2 / a * (b - x / a ** 2))
print(math.degrees(theta))
