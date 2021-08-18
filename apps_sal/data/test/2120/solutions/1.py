
n, m = [int(x) for x in input().split()]
v = [int(x) for x in input().split()]
sv = [(x + 1, v[x]) for x in range(n)]
v = [0] + v
edges = {i: set() for i in range(1, n + 1)}
for i in range(m):
    f, t = [int(x) for x in input().split()]
    edges[f].add(t)
    edges[t].add(f)

ans = 0
sv.sort(key=lambda x: -x[1])
removed = [False] * (n + 1)
for i, vi in sv:
    removed[i] = True
    for f in edges[i]:
        if not removed[f]:
            ans += v[f]

print(ans)
