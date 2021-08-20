import math
(n, r) = map(int, input().split())
a = math.pi / n
sin = math.sin(a)
R = r * sin / (1 - sin)
print(R)
