from itertools import combinations
from cmath import phase

N, *XY = map(int, open(0).read().split())

XY = sorted((complex(x, y) for x, y in zip(*[iter(XY)] * 2)), key=phase)
XY += XY


ans = 0
for i, j in combinations(range(2 * N + 1), 2):
    if j - i <= N:
        ans = max(ans, abs(sum(XY[i:j])))

print(ans)
