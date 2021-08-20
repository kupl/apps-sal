def dfs(pi):
    if len(pi) == n:
        p.append(pi)
        return
    for i in range(1, n + 1):
        if i in pi:
            continue
        cpi = pi + (i,)
        dfs(cpi)


n = int(input())
p = []
dfs(tuple())
pos = []
pos.append(-1)
for i in range(n):
    (x, y) = list(map(int, input().split()))
    pos.append((x, y))
dist = 0
for v in p:
    d = 0
    for i in range(len(v) - 1):
        pos1 = v[i]
        pos2 = v[i + 1]
        (xi, yi) = pos[pos1]
        (xj, yj) = pos[pos2]
        d += ((xi - xj) ** 2 + (yi - yj) ** 2) ** (1 / 2)
    dist += d
print(dist / len(p))
