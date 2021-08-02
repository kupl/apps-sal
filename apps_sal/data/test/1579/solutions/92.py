def get_group(x):
    g = group[x]
    if g == x:
        return x
    group[g] = re = get_group(g)
    return re


def unite(x, y):
    gx = get_group(x)
    gy = get_group(y)
    if gx != gy:
        dx = depth[gx]
        dy = depth[gy]
        if dy > dx:
            gx, gy = gy, gx
        group[gy] = gx
        if dx == dy:
            depth[gx] += 1


n = int(input())
group = {}
depth = {}
edge = []
for _ in range(n):
    x, y = list(map(int, input().split()))
    group.setdefault(x, x)
    group.setdefault(-y, -y)
    depth.setdefault(x, 1)
    depth.setdefault(-y, 1)
    edge += [[x, -y]]

for x, y in edge:
    unite(x, y)

cnt = {}
for k in list(group.keys()):
    g = get_group(k)
    cnt.setdefault(g, [0, 0])
    if k > 0:
        cnt[g][0] += 1
    else:
        cnt[g][1] += 1

ans = 0
for cx, cy in list(cnt.values()):
    ans += cx * cy
print((ans - n))
