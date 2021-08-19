import math
(a, b) = list(map(int, input().split()))
ans = math.ceil((b - 1) / (a - 1))
print(ans)
