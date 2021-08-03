from collections import defaultdict as dfdict


def bfs(G, rail_connected=False):
    level = [1]
    visited = set([1])
    cnt = 0
    while len(level) > 0:
        nxtlevel = []
        for i in level:
            nxt = G[i] if not rail_connected else all_vertice - G[i]
            for j in nxt:
                if j not in visited:
                    if j == n:
                        cnt += 1
                        return cnt
                    else:
                        nxtlevel.append(j)
                        visited.add(j)
        level = nxtlevel
        cnt += 1
    return -1


n, m = [int(i) for i in input().split()]
rails = dfdict(set)
all_vertice = set([i + 1 for i in range(n)])
for _ in range(m):
    xt, yt = [int(i) for i in input().split()]
    rails[xt].add(yt)
    rails[yt].add(xt)

R = False
if n in rails[1]:
    R = True
else:
    R = False

print(bfs(rails, R))
