from itertools import groupby, accumulate, product, permutations, combinations
import numpy as np
(N, M) = map(int, input().split())
adj = np.zeros((N, N), np.int64)
for i in range(M):
    (a, b) = map(lambda x: int(x) - 1, input().split())
    adj[a, b] = 1
    adj[b, a] = 1
ans = 0
for per in permutations(range(1, N), N - 1):
    if adj[0, per[0]] == 0:
        continue
    for i in range(N - 2):
        if adj[per[i], per[i + 1]] == 0:
            break
    else:
        ans += 1
print(ans)
