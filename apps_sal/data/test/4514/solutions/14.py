n, q = [int(x) for x in input().split(" ")]
parent = [-1] + [int(x) - 1 for x in input().split(" ")]
start = [0] * n
path = [0] * n
end = [1] * n
size = [1] * n

for i in range(n - 1, 0, -1):
    size[parent[i]] += size[i]

for v in range(1, n):
    start[v] = end[parent[v]]
    end[v] = start[v] + 1
    end[parent[v]] += size[v]
    path[start[v]] = v

for j in range(q):
    u, k = [int(x) - 1 for x in input().split(" ")]
    print(-1 if k >= size[u] else path[start[u] + k] + 1)
