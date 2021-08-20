import math
(a, b, x) = map(int, input().split())
if x <= a ** 2 * b / 2:
    n = 2 * x / (a * b)
    ans = math.acos(n / math.sqrt(b ** 2 + n ** 2))
else:
    n = 2 * b - 2 * x / a ** 2
    ans = math.acos(a / math.sqrt(a ** 2 + n ** 2))
print(math.degrees(ans))
