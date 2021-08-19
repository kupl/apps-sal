import math
(a, b, x) = map(int, input().split())
if x >= a ** 2 * b / 2:
    y = 2 * (a ** 2 * b - x) / a ** 2
    ans = math.degrees(math.atan(y / a))
else:
    y = 2 * x / (a * b)
    ans = math.degrees(math.atan(b / y))
print(ans)
