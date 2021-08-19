import math
(a, b, x) = list(map(int, input().split()))
vol = a * a * b
if x <= vol // 2:
    tmp = 2 * x / (a * b)
    ans = math.atan(b / tmp)
else:
    tmp = 2 * x / a ** 2 - b
    tmp = b - tmp
    ans = math.atan(tmp / a)
print(math.degrees(ans))
