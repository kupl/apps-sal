import math
A, B, H, M = map(int, input().split())

s = float(max(6 * M, 30 * H + 1 / 2 * M) - min(6 * M, 30 * H + 1 / 2 * M)) / 180 * math.pi
S = float(min(s, abs(s - 180)) / 180 * math.pi)
print(float(math.sqrt(A**2 + B**2 - 2 * A * B * math.cos(s))))
