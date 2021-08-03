N, M = map(int, input().split())
LRD = [tuple(int(x) for x in input().split()) for _ in range(M)]
Graph = [[] for _ in range(N)]
for l, r, d in LRD:
    Graph[r - 1].append((l - 1, d))
    Graph[l - 1].append((r - 1, -d))

seen = set()
Dfr = [0] * N  # dist from Root
for root in range(N):
    if root in seen:
        continue
    seen.add(root)
    V = [root]
    while len(V) != 0:  # bfs
        v = V.pop(0)
        for nv, d in Graph[v]:
            if nv in seen and Dfr[nv] != Dfr[v] + d:  # bfsで発見済みの値が異なる⇔矛盾
                print('No')
                return
            if nv in seen:
                continue
            else:
                seen.add(nv)
                Dfr[nv] = Dfr[v] + d
                V.append(nv)
print('Yes')
