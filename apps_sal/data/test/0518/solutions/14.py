import math
(n, r) = map(int, input().split())
print(r / (1 / math.cos(math.pi * (n - 2) / 2 / n) - 1))
