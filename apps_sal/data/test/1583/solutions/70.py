import math
(a, b, x) = map(int, input().split())
c = 2 * x / (a * b)
if c <= a:
    ans = 90 - math.degrees(math.atan(c / b))
else:
    d = 2 * (a ** 2 * b - x) / a ** 2
    if d == 0:
        ans = 0
    else:
        ans = 90 - math.degrees(math.atan(a / d))
print(ans)
