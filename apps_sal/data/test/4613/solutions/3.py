(n, m) = map(int, input().split())
AB = [list(map(int, input().split())) for _ in range(m)]


def find(x):
    if root[x] < 0:
        return x
    else:
        root[x] = find(root[x])
        return root[x]


def unit(x, y):
    gx = find(x)
    gy = find(y)
    if gx == gy:
        return
    if root[gx] > root[gy]:
        (gx, gy) = (gy, gx)
    root[gx] += root[gy]
    root[gy] = gx


cnt = 0
for i in range(m):
    root = [-1] * n
    for j in range(m):
        if i == j:
            continue
        unit(AB[j][0] - 1, AB[j][1] - 1)
    roots = [i for i in root if i < 0]
    cnt += len(roots) != 1
print(cnt)
