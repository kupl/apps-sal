from numpy.linalg import det
from numpy.linalg import solve
import numpy as np
import math


def find_cross_point(x1, y1, x2, y2, x3, y3):
    A = np.array([[x2 - x1, y2 - y1], [x3 - x2, y3 - y2]])
    B = np.array([(x2**2 + y2**2 - x1**2 - y1**2) / 2, (x3**2 + y3**2 - x2**2 - y2**2) / 2])
    if det(A) == 0:
        return (float("inf"), float("inf"))
    C = solve(A, B)
    return C


N = int(input())
ans = 10**10
plots = []


for i in range(N):
    x, y = list(map(int, input().split()))
    plots.append((x, y))


for i in range(N):
    for j in range(i + 1, N):
        sub = 0
        m_x, m_y = (plots[i][0] + plots[j][0]) / 2, (plots[i][1] + plots[j][1]) / 2
        for k in range(N):
            sub = max(sub, math.hypot(m_x - plots[k][0], m_y - plots[k][1]))
        ans = min(ans, sub)


for i in range(N):
    for j in range(i + 1, N):
        for k in range(j + 1, N):
            sub = 0
            x1, y1 = plots[i]
            x2, y2 = plots[j]
            x3, y3 = plots[k]
            m_x, m_y = find_cross_point(x1, y1, x2, y2, x3, y3)
            for p in range(N):
                sub = max(sub, math.hypot(m_x - plots[p][0], m_y - plots[p][1]))
            ans = min(ans, sub)
print(ans)
