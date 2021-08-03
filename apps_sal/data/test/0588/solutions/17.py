import numpy as np
n = int(input())
xy = [tuple(map(int, input().split())) for _ in range(n)]
e = (1, 0)
xyz = []
k = 0
for x, y in xy:
    if x == 0 and y == 0:
        continue
    k += 1
    l = np.linalg.norm((x, y))
    z = np.inner((x / l, y / l), e)
    theta = np.rad2deg(np.arccos(z))
    if y < 0:
        theta = 360 - theta
    xyz.append((x, y, theta))
xyz.sort(key=lambda x: x[2])


tx, ty = 0, 0
c = [(0, 0)]
for x, y, z in xyz:
    tx += x
    ty += y
    c.append((tx, ty))
for x, y, z in xyz:
    tx += x
    ty += y
    c.append((tx, ty))

ans = 0
for i in range(k):
    for j in range(k):
        x = c[i + j + 1][0] - c[i][0]
        y = c[i + j + 1][1] - c[i][1]
        ans = max(ans, (x**2 + y**2)**0.5)
print(ans)
