import math
A, B, H, M = map(float, input().split())
rad_min = 2.0 * math.pi * M / 60
rad_hour = 2.0 * math.pi * H / 12.0 + math.pi / 6.0 * M / 60.0
rad = abs(rad_min - rad_hour)
l = math.sqrt(A**2 + B**2 - 2.0 * A * B * math.cos(rad))
print(l)
