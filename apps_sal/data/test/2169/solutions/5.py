import numpy as np
H, W, D = map(int, input().split())
Aindex = [0] * (H * W)
for h in range(H):
    w = 0
    for A in input().split():
        Aindex[int(A) - 1] = (h, w)
        w += 1

v, h = int(np.ceil(H * W / D)), D
Mp = np.zeros((v, h))
def mp(X, Y): return abs(X[0] - Y[0]) + abs(X[1] - Y[1])


for x in range(D, H * W):
    i, j = divmod(x, D)
    Mp[i, j] = mp(Aindex[x], Aindex[x - D])
Mp = Mp.cumsum(axis=0)

Q = int(input())
Query = [(int(x) for x in input().split()) for _ in range(Q)]
for l, r in Query:
    ans = Mp[divmod(r - 1, D)] - Mp[divmod(l - 1, D)]
    print(int(ans))
