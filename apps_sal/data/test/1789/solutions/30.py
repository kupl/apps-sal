import math
(a, b, x, y) = map(int, input().split())
t = min(2 * x, y)
d = abs(2 * b + 1 - 2 * a)
print(math.floor(d / 2) * t + x)
