import math
(c, x, y, a, b) = list(map(int, input().split()))
lim = int(math.sqrt(c))
ans = 0
for i in range(lim):
    if c >= i * a:
        ans = max(ans, x * i + (c - i * a) // b * y)
    if c >= i * b:
        ans = max(ans, y * i + (c - i * b) // a * x)
print(ans)
