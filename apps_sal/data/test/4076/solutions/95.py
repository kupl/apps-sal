import math
A, B, H, M = list(map(int, input().split()))
theta = (M * 11 / 360 - H / 6) * math.pi
print(((A ** 2 + B ** 2 - 2 * A * B * math.cos(theta)) ** 0.5))
return

