import sys
from fractions import gcd
n, x, d = map(int, input().split())

if x == 0 and d == 0:
    print(1)
    return
elif d == 0:
    print(n + 1)
    return

if x < 0 and x + (n - 1) * d < 0:
    x, d = -x, -d

if x >= 0 and d < 0:
    x, d = x + (n - 1) * d, -d

g = gcd(x, d)

ans = 1
if x >= 0:
    for i in range(1, n + 1):
        k = max((i - d // g) * (2 * n - 1 - i + d // g) // 2 - x // g, i * (i - 1) // 2 - 1)
        ans += max((i * (2 * n - 1 - i)) // 2 - k, 0)

else:
    for i in range(1, n + 1):
        overlap_u = min((i - d // g) * (2 * n - 1 - i + d // g) // 2 - x // g, i * (2 * n - 1 - i) // 2)
        overlap_l = max((i - d // g) * (i - d // g - 1) // 2 - x // g, i * (i - 1) // 2)
        ans += i * (2 * n - 1 - i) // 2 - i * (i - 1) // 2 + 1 - max(overlap_u - overlap_l + 1, 0)

print(ans)
