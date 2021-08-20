import math
(A, B, H, M) = list(map(int, input().split()))
theta = abs((H + M / 60) / 12 - M / 60) * 2 * math.pi
ans = math.sqrt(A * A + B * B - 2 * A * B * math.cos(theta))
print(ans)
