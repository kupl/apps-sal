import math
(n, r) = [int(x) for x in input().split()]
x = math.sin(math.pi / n)
y = x * r / (1 - x)
print(y)
