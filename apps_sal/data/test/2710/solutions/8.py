class edge:
    def __init__(self, node, capacity, flow, rev):
        self.node = node
        self.capacity = capacity
        self.flow = flow
        self.rev = rev

    def __str__(self):
        return (",".join([str(x) for x in
                          [self.node,
                           self.capacity,
                           self.flow]])
                if self.capacity else "Back Edge")


class flow:
    def __init__(self, n):
        self.n = n
        self.g = [[] for _ in range(n)]

    def adde(self, u, v, w):
        x = edge(v, w, 0, None)
        y = edge(u, 0, 0, x)
        x.rev = y
        self.g[u].append(x)
        self.g[v].append(y)

    def dfs(self, u, t, bottleneck):
        if u == t:
            return bottleneck
        self.visited[u] = True
        for e in self.g[u]:
            v = e.node
            residual = e.capacity - e.flow
            if residual > 0 and not self.visited[v]:
                augment = self.dfs(v, t, min(bottleneck, residual))
                if augment > 0:
                    e.flow += augment
                    e.rev.flow -= augment
                    return augment
        return 0

    def max_flow(self, s, t):
        flow = 0
        augment = 0
        while True:
            self.visited = [False for _ in range(self.n)]
            augment = self.dfs(s, t, float('inf'))
            flow += augment
            if augment <= 0:
                break
        return flow

    def reprnode(self, u):
        sz = self.n // 2 - 1
        rpr = [0] * (sz)
        for e in self.g[u]:
            if e.capacity:
                try:
                    rpr[e.node - sz - 1] = e.flow
                except:
                    pass
        return " ".join([str(x) for x in rpr])


def __starting_point():
    n, m = [int(x) for x in input().split()]
    s = 0
    t = 2 * n + 1
    f = flow(t + 1)
    atot = 0
    btot = 0
    array_a = [int(x) for x in input().split()]
    array_b = [int(x) for x in input().split()]
    for i, (a, b) in enumerate(zip(array_a, array_b), start=1):
        f.adde(s, i, a)
        f.adde(i + n, t, b)
        f.adde(i, i + n, float('inf'))
        atot += a
        btot += b
    for _ in range(m):
        p, q = [int(x) for x in input().split()]
        f.adde(p, q + n, float('inf'))
        f.adde(q, p + n, float('inf'))
    if atot == f.max_flow(s, t) and atot == btot:
        print("YES")
        for i in range(1, n + 1):
            print(f.reprnode(i))
    else:
        print("NO")


__starting_point()
