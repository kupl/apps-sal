import numpy as np
N = int(input())
XY = np.array([list(map(int, input().split())) for _ in [0] * N])
th = np.arctan2(XY[:, 1], XY[:, 0])
XY = XY[th.argsort()]
ans = 0
n = np.linalg.norm
Sxy = np.vstack((np.zeros(2), np.cumsum(XY, axis=0)))
i = 0
j = 1
pr = 0
while i < N:
    r = n(Sxy[min(j, N)] - Sxy[i] + Sxy[max(0, j - N)])
    if r >= pr and j < i + N + 1:
        j += 1
    else:
        i += 1
        j = max(j - 1, i + 1)
        r = 0
    ans = max(ans, r)
    pr = r
print(ans)
