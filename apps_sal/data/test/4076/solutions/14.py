import math
(A, B, H, M) = map(int, input().split())
angle = H * 30 + 30 * (M / 60) - M * 6
abs_angle = abs(angle)
if abs_angle > 180:
    abs_angle = 360 - abs_angle
abs_angle = math.cos(math.radians(abs_angle))
ans_sqrt = A ** 2 + B ** 2 - 2 * A * B * abs_angle
print(math.sqrt(ans_sqrt))
