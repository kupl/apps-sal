class mergefind:

    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_sets = n

    def find(self, a):
        to_update = []
        while a != self.parent[a]:
            to_update.append(a)
            a = self.parent[a]
        for b in to_update:
            self.parent[b] = a
        return self.parent[a]

    def merge(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return
        if self.size[a] < self.size[b]:
            (a, b) = (b, a)
        self.num_sets -= 1
        self.parent[b] = a
        self.size[a] += self.size[b]

    def set_size(self, a):
        return self.size[self.find(a)]

    def __len__(self):
        return self.num_sets


def toposort(C, n):
    indeg = [0] * n
    for (i, neighs) in enumerate(C):
        for neigh in neighs:
            indeg[neigh] += 1
    S = [i for i in range(n) if indeg[i] == 0]
    nparent = indeg[:]
    topo = []
    while S:
        cur = S.pop()
        topo.append(cur)
        for neigh in C[cur]:
            nparent[neigh] -= 1
            if nparent[neigh] == 0:
                S.append(neigh)
    return topo


(n, m) = map(int, input().split())
A = [input() for _ in range(n)]
mf = mergefind(n + m)
for i in range(n):
    for j in range(m):
        if A[i][j] == '=':
            mf.merge(i, n + j)
C = [set() for _ in range(n + m)]
for i in range(n):
    for j in range(m):
        if A[i][j] == '<':
            C[mf.find(i)].add(mf.find(n + j))
        elif A[i][j] == '>':
            C[mf.find(n + j)].add(mf.find(i))
D = [1] * (n + m)
for cur in toposort(C, n + m):
    for neigh in C[cur]:
        D[neigh] = max(D[neigh], D[cur] + 1)
D = [D[mf.find(i)] for i in range(n + m)]
ok = True
for i in range(n):
    for j in range(m):
        if A[i][j] == '<':
            if D[i] >= D[n + j]:
                ok = False
        elif A[i][j] == '>':
            if D[i] <= D[n + j]:
                ok = False
        elif D[i] != D[n + j]:
            ok = False
if ok:
    print('Yes')
    print(*D[:n])
    print(*D[n:])
else:
    print('No')
