from collections import deque, defaultdict
N = int(input())
ab = [list(map(int, input().split())) for _ in range(N - 1)]
d = [0] * (N + 1)
G = [[] for _ in range(N + 1)]
for a, b in ab:
    d[a] += 1
    d[b] += 1
    G[a].append(b)
    G[b].append(a)
print((max(d)))

color = defaultdict(int)
q = deque([[1, 0]])
seen = [0] * (N + 1)
while q:
    v, c = q.popleft()
    seen[v] = 1
    tem = 1
    for u in G[v]:
        if seen[u]:
            continue
        if tem == c:
            tem += 1
        q.append([u, tem])
        i, j = min(v, u), max(v, u)
        color[(i, j)] = tem
        tem += 1

for a, b in ab:
    i, j = min(a, b), max(a, b)
    print((color[(i, j)]))
