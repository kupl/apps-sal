import math
a, b, h, m = list(map(int, input().split()))
ans = math.sqrt(a * a + b * b - 2 * a * b * math.cos(math.pi * (h / 6 + m / 360 - m / 30)))
print(ans)
