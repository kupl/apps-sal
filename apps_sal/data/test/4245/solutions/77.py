import math
(a, b) = map(int, input().split())
ans = math.ceil((b - 1) / (a - 1))
print(ans)
