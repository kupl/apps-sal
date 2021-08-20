import numpy as np
(N, M, X) = map(int, input().split())
C = [list(map(int, input().split())) for _ in range(N)]
cost = float('inf')
for i in range(2 ** N):
    tmp = np.array([0 for _ in range(M + 1)])
    for j in range(N):
        if i >> j & 1:
            tmp += np.array(C[j])
    if min(tmp[1:]) >= X:
        cost = min(cost, tmp[0])
print(-1 if cost == float('inf') else cost)
