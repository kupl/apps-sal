import math
from fractions import gcd
l, r, x, y = list(map(int, input().strip().split()))
b = math.ceil(l / x)
e = r // x
if (y % x != 0):
    print(0)
    return
y = y / x
if (y == 1 and b == 1 and e >= 1):
    print(1)
    return
ans = 0
for i in range(1, math.ceil(math.sqrt(y))):
    if (y % i) == 0:
        d = y // i
        if (gcd(i, d) == 1 and i >= b and i <= e and d >= b and d <= e):
            if (i == d):
                ans = ans + 1
            else:
                ans = ans + 2
print(ans)
