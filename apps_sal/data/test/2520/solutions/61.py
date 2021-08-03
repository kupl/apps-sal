class UnionFind:
    def __init__(self, N):
        self.root = list(range(N + 1))
        self.size = [1] * (N + 1)

    def __getitem__(self, x):
        root = self.root
        while root[x] != x:
            root[x] = root[root[x]]
            x = root[x]
        return x

    def merge(self, x, y):
        x = self[x]
        y = self[y]
        if x == y:
            return
        sx, sy = self.size[x], self.size[y]
        if sx < sy:
            x, y = y, x
            sx, sy = sy, sx
        self.root[y] = x
        self.size[x] += sy


def graph_input(N, M):
    G = [[] for _ in range(N + 1)]
    for _ in range(M):
        a, b = list(map(int, input().split()))
        G[a].append(b)
        G[b].append(a)
    return G


N, M, K = list(map(int, input().split()))
friend = graph_input(N, M)
block = graph_input(N, K)

uf = UnionFind(N + 1)
for a in range(N + 1):
    for b in friend[a]:
        uf.merge(a, b)

answer = [0] * (N + 1)
for a in range(N + 1):
    n = uf.size[uf[a]] - 1
    for x in friend[a] + block[a]:
        if uf[a] == uf[x]:
            n -= 1
    answer[a] = n

print((' '.join(map(str, answer[1:]))))
