import math
[A, B, H, M] = [int(i) for i in input().split()]
x = 5.5 * (60 * H + M)
c = A**2 + B**2 - 2 * A * B * math.cos(math.radians(x))
print(c**0.5)
