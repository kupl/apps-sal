import math
import numpy as np

A, B, H, M = list(map(int, input().split()))

thetaA = math.radians(((H / 12) + (1 / 12 * M / 60)) * 360)
thetaB = math.radians(M / 60 * 360)

a = np.array([A * math.sin(thetaA), A * math.cos(thetaA)])
b = np.array([B * math.sin(thetaB), B * math.cos(thetaB)])

print((round(np.linalg.norm(a - b), 11)))

