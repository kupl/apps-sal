import math

A, B, H, M = map(int, input().split())

thetaA = (math.pi * H / 6) + (math.pi * M / 360)
thetaB = (math.pi * M / 30)
Ax = A * math.cos(thetaA)
Ay = A * math.sin(thetaA)
Bx = B * math.cos(thetaB)
By = B * math.sin(thetaB)

X = Ax - Bx
Y = Ay - By

ans = (X ** 2 + Y ** 2) ** 0.5

print(ans)
