import numpy as np
N = int(input())
XY = np.array([list(map(int, input().split())) for _ in [0] * N])
ans = 0
for m in range(100):
    th = 2 * np.pi * m / 100
    r = np.array([np.cos(th), np.sin(th)])
    check = XY.dot(r) >= 0
    ans = max(ans, np.linalg.norm(np.sum(XY[check], axis=0)))
print(ans)
