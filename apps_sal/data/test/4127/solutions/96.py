import math
(a, b) = list(map(float, input().split()))
a = int(a)
b = int(round(b * 100))
ans = a * b
ans = ans // 100
print(ans)
