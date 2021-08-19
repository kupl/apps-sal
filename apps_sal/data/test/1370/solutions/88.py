import numpy as np
from itertools import product
(H, W, K) = map(int, input().split())
G = np.array([list(map(int, input())) for _ in range(H)])
ans = float('inf')
for pattern in product([0, 1], repeat=H - 1):
    div = [0]
    for (i, p) in enumerate(pattern):
        if p == 1:
            div = div + [i + 1]
    div += [10]
    rows = []
    for i in range(len(div) - 1):
        rows.append(np.sum(G[div[i]:div[i + 1]], axis=0))
    count = 0
    for r in rows:
        if np.any(r > K):
            count = 1
    if count == 1:
        continue
    rows = [r.tolist() for r in rows]
    tmp_ans = 0
    counts = [0] * len(rows)
    w = 0
    while w < W:
        for r in range(len(rows)):
            counts[r] += rows[r][w]
        if any([c > K for c in counts]):
            counts = [0] * len(rows)
            w -= 1
            tmp_ans += 1
        w += 1
    a = tmp_ans + len(div) - 2
    ans = min(a, ans)
print(ans)
