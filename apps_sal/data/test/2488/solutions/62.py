from itertools import accumulate
import math
import bisect
(n, d, a) = map(int, input().split())
xh = [tuple(map(int, input().split())) for _ in range(n)]
xh.sort()
x = [xh[i][0] for i in range(n)]
h = [xh[i][1] for i in range(n)]
damage = [0] * (n + 1)
point = 0
for i in range(n):
    if i != 0:
        damage[i] += damage[i - 1]
    bi = bisect.bisect(x, 2 * d + x[i])
    count = max(math.ceil((h[i] - damage[i]) / a), 0)
    damage[i] += a * count
    damage[bi] -= a * count
    point += count
print(point)
