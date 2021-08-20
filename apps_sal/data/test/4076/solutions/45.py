import numpy as np
(A, B, H, M) = list(map(int, input().split()))
angle_h = 1.0 / 12.0 * (H + M / 60.0) * 2 * np.pi
angle_m = M / 60.0 * 2 * np.pi
hour = (A * np.sin(angle_h), A * np.cos(angle_h))
minute = (B * np.sin(angle_m), B * np.cos(angle_m))
dist = np.sqrt((hour[0] - minute[0]) ** 2 + (hour[1] - minute[1]) ** 2)
print(dist)
