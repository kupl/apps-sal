import math
(A, B, H, M) = map(int, input().split())
H_angle = M * math.pi / 30
M_angle = (60 * H + M) * math.pi / 360
(H_x, H_y) = (A * math.cos(H_angle), A * math.sin(H_angle))
(M_x, M_y) = (B * math.cos(M_angle), B * math.sin(M_angle))
d = math.sqrt((H_x - M_x) ** 2 + (H_y - M_y) ** 2)
print(d)
