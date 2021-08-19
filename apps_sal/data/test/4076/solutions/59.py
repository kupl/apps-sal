import numpy as np
(a, b, h, m) = map(int, input().split())
hour_theta = np.pi * (60 * h + m) / 360
minute_theta = np.pi * m / 30
theta = abs(hour_theta - minute_theta)
ans = np.sqrt(a ** 2 + b ** 2 - 2 * a * b * np.cos(theta))
print('{:.11f}'.format(ans))
