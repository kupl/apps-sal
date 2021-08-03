import itertools
from math import atan2, sqrt

N = int(input())
A = [t for _ in range(N) if (t := tuple(map(int, input().split()))) != (0, 0)]

A.sort(key=lambda x: atan2(x[1], x[0]))

# 向きが同じエンジンは１つにまとめる
Ax, Ay = [], []
for _, v in itertools.groupby(A, key=lambda x: atan2(x[1], x[0])):
    sx, sy = 0, 0
    for vx, vy in v:
        sx += vx
        sy += vy
    Ax.append(sx)
    Ay.append(sy)

Nu = len(Ax)

Ax = [0] + list(itertools.accumulate(Ax * 2))
Ay = [0] + list(itertools.accumulate(Ay * 2))

ans = 0
for i in range(Nu + 1):
    for j in range(i + 1, min(i + Nu + 1, 2 * Nu + 1)):
        ans = max(ans, (Ax[j] - Ax[i]) ** 2 + (Ay[j] - Ay[i]) ** 2)

print((sqrt(ans)))
