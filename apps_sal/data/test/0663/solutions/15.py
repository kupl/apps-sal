from math import hypot
(r, x, y, xn, yn) = map(int, input().split())
d = hypot(x - xn, y - yn)
ans = 0
if d == r or d == 0:
    print(0)
elif d < r:
    print(1)
else:
    mama = 0
    while mama < d:
        mama += 2 * r
        ans += 1
    print(ans)
