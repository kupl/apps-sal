import math

a, b, x = map(int, input().split())

if x / a >= a * b / 2:
    ans = math.atan((b - x / a / a) * 2 / a)
else:
    ans = math.atan(a * b * b / x / 2)
print(math.degrees(ans))
