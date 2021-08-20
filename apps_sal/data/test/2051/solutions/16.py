(n, m, k) = list(map(int, input().split()))
c = [int(x) - 1 for x in input().split()]
adj = [[] for _ in range(n)]
for _ in range(m):
    (l, r) = list(map(int, input().split()))
    adj[l - 1].append(r - 1)
    adj[r - 1].append(l - 1)
vis = [0] * n
ans = 0
for i in range(n):
    if vis[i] == 1:
        continue
    (arr, cur) = ([i], 0)
    while cur < len(arr):
        v = arr[cur]
        vis[v] = 1
        cur += 1
        for nv in adj[v]:
            if vis[nv] == 0:
                arr.append(nv)
                vis[nv] = 1
    d = {}
    for v in arr:
        d[c[v]] = d.get(c[v], 0) + 1
    ans += len(arr) - max(d.values())
print(ans)
