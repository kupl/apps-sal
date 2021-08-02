import numpy as np
n = int(input())
xy = np.array([list(map(int, input().split())) for _ in range(n)]).T
ans = 0
L = np.angle(xy[0] + xy[1] * 1j)
A = sorted([[j, xy[0][i], xy[1][i]] for i, j in enumerate(L)])
A = [i[1:] for i in A]
A = np.array(A * 2)
for i in range(n):
    for j in range(i + 1, i + n + 1):
        S = A[i:j]
        t = S.sum(axis=0)
        ans = max(ans, np.hypot(*t))
print(ans)
