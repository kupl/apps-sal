from itertools import permutations
from collections import Counter
(N, C) = map(int, input().split())
D = [list(map(int, input().split())) for i in range(C)]
E = [list(map(int, input().split())) for i in range(N)]
ctrs = [Counter() for _ in range(3)]
for (i, row) in enumerate(E):
    for (j, c) in enumerate(row):
        ctrs[(i + j) % 3][c] += 1
ans = float('inf')
for ptn in permutations(range(1, C + 1), 3):
    t = 0
    for (p, c) in zip(ptn, ctrs):
        for (k, v) in c.items():
            t += D[k - 1][p - 1] * v
    ans = min(ans, t)
print(ans)
