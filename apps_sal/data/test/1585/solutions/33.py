import math
(x, y) = map(int, input().split())
ans = 0
while y >= x:
    x = x * 2
    ans += 1
print(ans)
