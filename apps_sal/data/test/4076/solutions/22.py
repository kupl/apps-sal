import math
(A, B, H, M) = map(int, input().split())
at = (60 * H + M) / (12 * 60) * 2 * math.pi
bt = M / 60 * 2 * math.pi
ax = A * math.sin(at)
ay = A * math.cos(at)
bx = B * math.sin(bt)
by = B * math.cos(bt)
print(((ax - bx) ** 2 + (ay - by) ** 2) ** 0.5)
