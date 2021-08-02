# python template for atcoder1
import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline


class UnionFind:
    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.size = [1 for _ in range(N)]

    def find(self, x):
        if self.parent[x] == x:
            return x
        else:
            return self.find(self.parent[x])

    def union(self, x, y):
        px = self.find(x)
        py = self.find(y)
        if px == py:
            return
        if self.size[px] < self.size[py]:
            self.parent[px] = py
            self.size[py] += self.size[px]
        else:
            self.parent[py] = px
            self.size[px] += self.size[py]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def connectedNum(self, x):
        return self.size[self.find(x)]

    def component_NUM(self):
        par = set()
        for i in self.parent:
            par.add(self.find(i))
        return len(par)


N, M = list(map(int, input().split()))
adj = [set() for _ in range(N)]
Un = UnionFind(N)
for _ in range(M):
    a, b = [int(x) - 1 for x in input().split()]
    adj[a].add(b)
    adj[b].add(a)

added = set()
representative = set()
for i in range(N):
    if i in added:
        continue
    added.add(i)
    representative.add(i)
    for j in range(i + 1, N):
        if j in added:
            continue
        if adj[i] == adj[j]:
            added.add(j)
            Un.union(i, j)
    if len(representative) > 3:
        print(-1)
        return
if Un.component_NUM() == 3:
    group = {}
    ans = []
    for p in range(N):
        par = Un.find(p)
        if par not in list(group.keys()):
            group[par] = len(group) + 1
        ans.append(group[par])
    print(" ".join(map(str, ans)))
else:
    print(-1)
