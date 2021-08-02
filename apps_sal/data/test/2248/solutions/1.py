n, m = list(map(int, input().split()))
cn = {}
for i in range(1, n + 1):
    cn[i] = set()
for _ in range(m):
    a, b = list(map(int, input().split()))
    cn[a].add(b)
    cn[b].add(a)


def dfs(node):
    vs = set()
    q = [(0, node)]
    dist = 0
    fnode = node
    while q:
        d, node = q.pop()
        vs.add(node)
        if d > dist:
            dist, fnode = d, node
        for i in cn[node]:
            if i not in vs:
                q.append((d + 1, i))
    return dist, fnode


_, fnode = dfs(1)
print(dfs(fnode)[0])
