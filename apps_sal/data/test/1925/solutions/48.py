import math
a, b, n = map(int, input().split())
i = b - 1
if i > n:
    i = n
print(math.floor(a * i / b) - a * math.floor(i / b))
