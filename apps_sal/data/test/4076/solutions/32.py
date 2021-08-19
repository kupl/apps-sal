import math
(A, B, H, M) = map(int, input().split())
h = (H / 12 + M / 60 / 12) * 360
m = M / 60 * 360
r = min(abs(h - m), 360 - abs(h - m))
ans = (A ** 2 + B ** 2 - 2 * B * A * math.cos(math.radians(r))) ** (1 / 2)
print(ans)
