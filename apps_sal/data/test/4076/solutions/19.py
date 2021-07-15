import math
A, B, H, M = map(int, input().split())
thetaA = math.pi * (0.5*(H*60 + M)) / 180
thetaB = math.pi * 6.0*M / 180
theta = min(2*math.pi-abs(thetaA-thetaB), abs(thetaA-thetaB))
cosC = math.cos(theta)
ans = math.sqrt(A**2+B**2-2*A*B*cosC)
print(ans)
