(n, m) = list(map(int, input().split()))
e = [tuple(map(int, input().split())) for i in range(m)]
e = sorted(((w, u, v) for (u, v, w) in e))
(p, r) = ([i for i in range(n + 1)], [0] * (n + 1))


def find(x):
    if p[x] != x:
        p[x] = find(p[x])
    return p[x]


def union(x, y):
    (x, y) = (p[x], p[y])
    if r[x] < r[y]:
        p[x] = y
    else:
        p[y] = x
        if r[x] == r[y]:
            r[x] += 1


ans = 0
i = 0
while i < m:
    j = i + 1
    while j < m and e[j][0] == e[i][0]:
        j += 1
    tmp = [(u, v) for (w, u, v) in e[i:j] if find(u) != find(v)]
    for (u, v) in tmp:
        if find(u) == find(v):
            ans += 1
        else:
            union(u, v)
    i = j
print(ans)
