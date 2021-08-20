(n, m) = list(map(int, input().split()))
adj = {}
nincident = [0] * (n + 1)
edges = []
for i in range(1, n + 1):
    adj[i] = []
for i in range(m):
    (u, v) = list(map(int, input().split()))
    edges.append((u, v))
    adj[u].append(v)
    adj[v].append(u)
    nincident[u] += 1
    nincident[v] += 1
vmax = 0
for v in range(1, n + 1):
    if nincident[v] > nincident[vmax]:
        vmax = v
result = []
rank = [0] * (n + 1)
parent = [0] * (n + 1)


def make_set(i):
    rank[i] = 0
    parent[i] = i


def find_set(i):
    if i != parent[i]:
        parent[i] = find_set(parent[i])
    return parent[i]


def union_op(x, y):
    s_x = find_set(x)
    s_y = find_set(y)
    if rank[s_x] < rank[s_y]:
        parent[s_x] = s_y
    else:
        parent[s_y] = s_x
        if rank[s_y] == rank[s_x]:
            rank[s_x] += 1


for i in range(1, n + 1):
    make_set(i)
for u in adj[vmax]:
    result.append((u, vmax))
    union_op(u, vmax)
for e in edges:
    if find_set(e[0]) != find_set(e[1]):
        result.append(e)
        union_op(e[0], e[1])
for e in result:
    print(e[0], e[1])
