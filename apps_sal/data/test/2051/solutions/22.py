n, m, k = list(map(int, input().split()))
c = list(map(int, input().split()))
c = list([x-1 for x in c])
adj = [[] for _ in range(n)]
edges = list(list(map(int, input().split())) for _ in range(m))
for u, v in edges:
    u -= 1 ; v -= 1
    adj[u].append(v)
    adj[v].append(u)

vis = [0] * n
res = 0
for i in range(n):
    if vis[i] == 1: 
        continue
    arr, curr = [i], 0
    while curr < len(arr):
        u = arr[curr]
        vis[u] = 1
        curr += 1
        for v in adj[u]:
            if vis[v] == 0:
                arr.append(v)
                vis[v] = 1
    d = {}
    for j in arr:
        d[c[j]] = d.get(c[j], 0) + 1
    res += len(arr) - max(d.values())
print(res)

