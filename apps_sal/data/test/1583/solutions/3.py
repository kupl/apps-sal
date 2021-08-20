from math import pi, tan, atan, degrees
(a, b, x) = [int(i) for i in input().split()]
theta = pi * 0.5 - atan(2 * x / (a * b ** 2))
if b * tan(pi * 0.5 - theta) <= a:
    print(degrees(theta))
else:
    theta = atan(2 * b / a - 2 * x / a ** 3)
    print(degrees(theta))
