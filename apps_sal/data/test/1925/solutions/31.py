import math
(a, b, n) = map(int, input().split())
if n < b - 1:
    x = n
else:
    x = b - 1
ans = math.floor(a * x / b) - a * math.floor(x / b)
print(ans)
