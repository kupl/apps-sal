class Union:

    def __init__(self, n):
        self.p = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                self.p[x] = y
                self.rank[y] += self.rank[x]
            else:
                self.p[y] = x
                self.rank[x] += self.rank[y]


def push(g, u, v):
    if u not in g:
        g[u] = []
    if v not in g:
        g[v] = []
    g[u].append(v)
    g[v].append(u)


def push_c(cnt, u, i):
    if u not in cnt:
        cnt[u] = set()
    cnt[u].add(i)


def process(cnt, tup, deg0, order, g, U, u):
    if len(cnt[u]) > 0:
        i = next(iter(cnt[u]))
    else:
        return
    for v in tup[i]:
        cnt[v].remove(i)
        if len(cnt[v]) == 1:
            deg0.append(v)
    (v, w) = (None, None)
    for x in tup[i]:
        if x == u:
            continue
        if v is None:
            v = x
        else:
            w = x
    order.append(i)
    if U.find(u) != U.find(v):
        U.union(u, v)
        push(g, u, v)
    if U.find(u) != U.find(w):
        U.union(u, w)
        push(g, u, w)


def solve():
    n = int(input())
    tup = [list(map(int, input().split())) for _ in range(n - 2)]
    g = {}
    cnt = {}
    order = []
    for (i, [u, v, w]) in enumerate(tup):
        push_c(cnt, u, i)
        push_c(cnt, v, i)
        push_c(cnt, w, i)
    U = Union(n)
    deg0 = [x for (x, num) in list(cnt.items()) if len(num) == 1]
    while len(deg0) > 0:
        u = deg0.pop()
        process(cnt, tup, deg0, order, g, U, u)
    used = [0] * (n - 2)
    for i in order:
        used[i] = 1
    for (i, x) in enumerate(used):
        if x == 0:
            order.append(i)
    circle = []
    used = [0] * (n + 1)
    for u in g:
        if len(g[u]) == 1:
            circle.append(u)
            used[u] = 1
            break
    i = 0
    while i < len(circle):
        u = circle[i]
        for v in g[u]:
            if used[v] == 0:
                used[v] = 1
                circle.append(v)
        i += 1
    print(' '.join([str(x) for x in circle]))
    print(' '.join([str(x + 1) for x in order]))


for _ in range(int(input())):
    solve()
