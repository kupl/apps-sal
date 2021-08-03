# ABC 144 D
import math
[a, b, x] = [int(i) for i in input().split()]
if x <= (a**2) * b / 2:
    t = (a * b**2) / (2 * x)
    theta = math.atan(t)
else:
    t = (2 * b) / a - (2 * x) / a**3
    theta = math.atan(t)
print(math.degrees(theta))
