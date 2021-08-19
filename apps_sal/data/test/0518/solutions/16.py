import math
(n, r) = [int(i) for i in input().split()]
t = math.sin(math.pi / n)
res = r * t / (1 - t)
print(res)
