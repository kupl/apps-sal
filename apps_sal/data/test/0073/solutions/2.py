import math
(c, v0, v1, a, l) = list(map(int, input().split()))
n = 0
ans = 0
while n < c:
    ans += 1
    if n > 0:
        n -= l
    n += v0
    if v0 < v1:
        v0 = min(v0 + a, v1)
print(ans)
