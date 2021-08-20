import math
(A, B, H, M) = list(map(int, input().split()))
rad = (H / 12 - M * 11 / 720) * 2 * math.pi
ans = (A ** 2 + B ** 2 - 2 * A * B * math.cos(rad)) ** (1 / 2)
print(ans)
