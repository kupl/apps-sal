from collections import defaultdict, deque
 
 
def bfs(start):
    q = deque([start])
    dist = [-1] * N
    dist[start] = 0
    while q:
        v = q.popleft()
        for nv, nw in g[v]:
            if dist[nv] >= 0:
                continue
            dist[nv] = (dist[v] + nw) % 2
            q.append(nv)
    return dist
 
 
N, *UVW = map(int, open(0).read().split())
g = defaultdict(set)
 
ans = [0] * N
for u, v, w in zip(*[iter(UVW)] * 3):
    u -= 1
    v -= 1
    g[u].add((v, w))
    g[v].add((u, w))
print("\n".join(map(str, bfs(0))))
