import sys
from itertools import accumulate, combinations
from math import atan2
read = sys.stdin.read
(N, *xy) = map(int, read().split())
xy = sorted(zip(*[iter(xy)] * 2), key=lambda x: atan2(x[1], x[0]))
xy = [(0, 0)] + xy
xy *= 2
xy = list(zip(*map(list, map(accumulate, zip(*xy)))))
answer = 0
for n in range(N + 1):
    for (i, j) in combinations(range(n, n + N + 1), 2):
        (x1, y1) = xy[i]
        (x2, y2) = xy[j]
        candidate = (x1 - x2) ** 2 + (y1 - y2) ** 2
        if candidate > answer:
            answer = candidate
print(answer ** 0.5)
