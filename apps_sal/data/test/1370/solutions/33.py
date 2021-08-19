import numpy as np
import itertools
H, W, K = [int(_) for _ in input().split()]
S = np.zeros((H + 1, W + 1), dtype=int)
S[1:, 1:] = [[int(_) for _ in input()] for _ in range(H)]
cum = S.cumsum(axis=0).cumsum(axis=1)
# sum(a,b -> x,y) (1-indexed)
# cum[x][y]+cum[a-1][b-1]-cum[a-1][y]-cum[x][b-1]
ans = 10**10
for bs in itertools.product([True, False], repeat=H - 1):
    bs = [True] + list(bs) + [True]
    idxs = []
    for i, b in enumerate(bs):
        if b:
            idxs += [i]
    cum2 = np.array([cum[i2] - cum[i1] for i1, i2 in zip(idxs, idxs[1:])])
    i = 0
    cnt = sum(bs) - 3
    while i < W:
        di = min(
            np.searchsorted(c[i + 1:] - c[i], K, side='right') for c in cum2)
        if di == 0:
            cnt = 10**10
            break
        i += di
        cnt += 1
    ans = min(ans, cnt)
print(ans)
