# itne me hi thakk gaye?
n, q = list(map(int, input().split()))
parent = [-1] + [int(x) - 1 for x in input().split()]
# parent = [i-1 for i in parent]
start = [0 for i in range(n)]
end = [1 for i in range(n)]
size = [1 for i in range(n)]
path = [0 for i in range(n)]
for i in range(n - 1, 0, -1):
    size[parent[i]] += size[i]
for v in range(1, n):
    start[v] = end[parent[v]]
    end[v] = start[v] + 1
    end[parent[v]] += size[v]
    path[start[v]] = v
for j in range(q):
    u, k = [int(x) - 1 for x in input().split()]
    if k >= size[u]:
        print(-1)
    else:
        print(path[start[u] + k] + 1)
