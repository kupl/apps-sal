import math
a, b, n = map(int, input().split())
d = min(b - 1, n)
print(math.floor(a * d / b) - a * math.floor(d / b))
