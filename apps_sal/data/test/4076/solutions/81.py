import math
(A, B, H, M) = map(int, input().split())
theta = abs((0.5 * (H * 60 + M) - 6 * M) % 360)
if theta > 180:
    theta = 360 - theta
C = math.sqrt(A ** 2 + B ** 2 - 2 * A * B * math.cos(theta / 180 * math.pi))
print(C)
