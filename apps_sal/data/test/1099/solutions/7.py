import sys
from collections import defaultdict


def rl():
    return sys.stdin.readline().strip()


def BFS(s, nbrs):
    level = defaultdict(int)
    ind = 0
    level[ind] += 1
    frontier = [s]
    visited = {s}
    while frontier:
        next = []
        ind += 1
        for u in frontier:
            for v in nbrs[u]:
                if v not in visited:
                    next.append(v)
                    visited.add(v)
                    level[ind] += 1
        frontier = next
    return level


n = int(rl())
vert = []
nbrs = defaultdict(list)
for i in range(n - 1):
    vert.append(list(map(int, rl().split())))
    j = vert[-1][0]
    k = vert[-1][1]
    nbrs[j].append(k)
    nbrs[k].append(j)
new = 0
counter = BFS(1, nbrs)
for i in range(2, n - 1, 2):
    new += counter[i]
ans = min(n - 2 - new, new)
print(ans)
