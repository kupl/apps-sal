import math
(a, b, n) = map(int, input().split())
if n >= b:
    x = b - 1
else:
    x = n
print(math.floor(a * x / b))
