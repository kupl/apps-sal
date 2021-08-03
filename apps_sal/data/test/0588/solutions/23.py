import sys
from math import atan2, pi

n = int(input())
angles = []
engines = []
pi2 = 2 * pi
for i, line in enumerate(sys.stdin):
    x, y = list(map(int, line.split()))
    angle = atan2(y, x)
    angles.append((angle, i))  # -pi~pi
    angles.append((angle + pi2, i))  # pi~3pi
    engines.append(x + y * 1j)
angles.sort()

r = 0
tmp = 0
total = sum(engines)
ans = 0
for l in range(n):
    angle, i = angles[l]
    limit = angle + pi - 1e-9
    while angles[r][0] < limit:
        tmp += engines[angles[r][1]]
        r += 1
    ans = max(ans, abs(tmp), abs(total - tmp))
    tmp -= engines[i]
print(ans)
