import math
(a, b, x) = map(int, input().split())
x = x / a
if x >= a * b / 2:
    K = (a * b - x) / a * 2
    L = K / math.sqrt(K ** 2 + a ** 2)
    ans = math.degrees(math.asin(L))
    print(ans)
else:
    K = 2 * x / b
    L = b / math.sqrt(K ** 2 + b ** 2)
    ans = math.degrees(math.asin(L))
    print(ans)
