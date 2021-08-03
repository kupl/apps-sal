import math
A, B, H, M = map(int, input().split())
C2 = A**2 + B**2 - 2 * A * B * math.cos((30 * H - 11 * M / 2) / 180 * math.pi)
print(C2**(1 / 2))
