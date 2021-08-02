import math
a, b, h, m = map(int, input().split())
theta_h = 2 * math.pi * (h + m / 60) / 12
theta_m = 2 * math.pi * m / 60
d_theta = abs(theta_h - theta_m)
answer = math.sqrt(a**2 + b**2 - 2 * a * b * math.cos(d_theta))
print(answer)
