import math

a, b, x = [int(_) for _ in input().split()]

h = x / a / a
if a * b / 2 < a * h:
    theta = math.atan(2 * (b - h) / a)
else:
    theta = math.atan(b * b / a / h / 2)

ans = math.degrees(theta)
print(ans)
