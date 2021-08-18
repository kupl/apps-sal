from collections import defaultdict
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**7)


class UnionFind:
    def __init__(self, n):
        self.parent = [i for i in range(n)]

    def root(self, x):
        if self.parent[x] == x:
            return x
        else:
            self.parent[x] = self.root(self.parent[x])
            return self.parent[x]

    def unite(self, x, y):
        x = self.root(x)
        y = self.root(y)
        if x != y:
            self.parent[x] = y

    def same(self, x, y):
        return self.root(x) == self.root(y)


N, K, L = list(map(int, input().split()))
un = UnionFind(N)
for i in range(K):
    p, q = list(map(int, input().split()))
    p -= 1
    q -= 1
    un.unite(p, q)
G = [[] for i in range(N)]
for i in range(L):
    r, s = list(map(int, input().split()))
    r -= 1
    s -= 1
    G[r].append(s)
    G[s].append(r)
done = [False] * N
D = []
gid = 0


def dfs(i, gid):
    D[gid][un.root(i)] += 1
    done[i] = True
    for nex in G[i]:
        if done[nex]:
            continue
        dfs(nex, gid)


for i in range(N):
    if not done[i]:
        D.append(defaultdict(int))
        dfs(i, gid)
        gid += 1
ans = [0] * N
done = [False] * N
gid = 0


def dfs2(i, gid):
    done[i] = True
    ans[i] = D[gid][un.root(i)]
    for nex in G[i]:
        if done[nex]:
            continue
        dfs2(nex, gid)


for i in range(N):
    if not done[i]:
        dfs2(i, gid)
        gid += 1
print((*ans))
