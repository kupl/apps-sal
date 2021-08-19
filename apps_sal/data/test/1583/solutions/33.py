import math
(a, b, x) = list(map(int, input().strip().split()))
if a * a * b / 2 < x:
    res = b
    res -= x / (a * a)
    res *= 2
    res /= a
else:
    res = a * b * b
    res /= 2 * x
res = math.atan(res)
res = math.degrees(res)
print(res)
