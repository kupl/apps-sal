import math
m, b = list(map(int, input().split()))
ans = 0
for y in range(b + 1):
    x = m * (b - y)
    p = ((x + 1) * (y + 1) * (x + y)) // 2
    ans = max(ans, p)
print(ans)
