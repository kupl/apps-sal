import math
x = int(input())
res = 1
for b in range(2, math.ceil(math.sqrt(x))):
    p = 2
    while b ** (p + 1) <= x:
        p += 1
    res = max(res, b ** p)
print(res)
