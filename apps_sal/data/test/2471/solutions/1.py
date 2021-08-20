from itertools import product
from collections import defaultdict, Counter
(h, w, n) = map(int, input().split())
dic = defaultdict(int)
for _ in range(n):
    (y, x) = map(int, input().split())
    for (i, j) in product([-1, 0, 1], repeat=2):
        nx = x + i
        ny = y + j
        if 2 <= nx <= w - 1 and 2 <= ny <= h - 1:
            dic[nx, ny] += 1
c = Counter(dic.values())
c[0] = (w - 2) * (h - 2) - sum(c.values())
for i in range(10):
    print(c[i])
