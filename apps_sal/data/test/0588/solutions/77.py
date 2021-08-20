import cmath
import math
N = int(input())
Engines = []
ans = 0
(sumx, sumy) = (0, 0)
for _ in range(N):
    (x, y) = map(int, input().split())
    z = complex(x, y)
    arg_deg = cmath.phase(z)
    sumx += x
    sumy += y
    Engines.append((arg_deg, x, y))
ans = max(ans, math.hypot(sumx, sumy))
Engines.sort()
for i in range(N):
    for j in range(i, N):
        sub_x = 0
        sub_y = 0
        for k in range(i, j + 1):
            (deg, dx, dy) = Engines[k]
            sub_x += dx
            sub_y += dy
        ans = max(ans, math.hypot(sub_x, sub_y))
        ans = max(ans, math.hypot(sumx - sub_x, sumy - sub_y))
print(ans)
