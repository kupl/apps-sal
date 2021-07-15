import math

A, B, H, M = map(int, input().split())

M_deg = M / 60 * 360
H_deg = (H / 12 * 360) + (M_deg / 12)


deg = min(abs(H_deg - M_deg), abs(M_deg - H_deg))

rad = math.radians(deg)

ans = math.sqrt(A ** 2 + B ** 2 - 2 * A * B * math.cos(rad))

print(ans)
