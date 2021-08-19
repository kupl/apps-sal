import math
(n, x, t) = map(int, input().split())
a = math.ceil(n / x)
print(a * t)
