import math
(a, b, x) = list(map(int, input().split()))
ans = 0
if a ** 2 * b < 2 * x:
    ans = math.degrees(math.atan2(2 * (a ** 2 * b - x), a ** 3))
else:
    ans = math.degrees(math.atan2(a * b ** 2, 2 * x))
print(ans)
