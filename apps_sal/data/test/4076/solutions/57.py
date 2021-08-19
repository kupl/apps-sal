import math
(A, B, H, M) = map(int, input().split())
Btheta = M * math.pi / 30
Bx = B * math.cos(Btheta)
By = B * math.sin(Btheta)
Atheta = (60 * H + M) / 360 * math.pi
Ax = A * math.cos(Atheta)
Ay = A * math.sin(Atheta)
print(((Ax - Bx) ** 2 + (Ay - By) ** 2) ** (1 / 2))
