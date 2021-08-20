class DSU:

    def __init__(self, n):
        self.parents = [-1] * n
        self.size = [0] * n

    def make(self, v):
        if self.parents[v] != -1:
            return
        self.parents[v] = v
        self.size[v] = 1

    def find(self, v):
        if self.parents[v] in (v, -1):
            return self.parents[v]
        self.parents[v] = self.find(self.parents[v])
        return self.parents[v]

    def join(self, v, u):
        v = self.find(v)
        u = self.find(u)
        if v == u or -1 in (u, v):
            return
        if self.size[v] < self.size[u]:
            (v, u) = (u, v)
        self.parents[u] = v
        self.size[v] += self.size[u]


def get_cart2line(m):
    return lambda x, y: x * m + y


def main():
    (n, m, k) = map(int, input().split())
    g = [list(input()) for _ in range(n)]
    ocean = 0
    dsu = DSU(n * m)
    dsu.make(ocean)
    line = get_cart2line(m)
    for i in range(n):
        (a, b) = (line(i, 0), line(i, m - 1))
        dsu.make(a)
        dsu.make(b)
        dsu.join(ocean, a)
        dsu.join(ocean, b)
    for i in range(m):
        (a, b) = (line(0, i), line(n - 1, i))
        dsu.make(a)
        dsu.make(b)
        dsu.join(ocean, a)
        dsu.join(ocean, b)
    for i in range(n):
        for j in range(m):
            if g[i][j] == '.':
                dsu.make(line(i, j))
                if j > 0:
                    if g[i][j - 1] == '.':
                        dsu.join(line(i, j - 1), line(i, j))
                if i > 0:
                    if g[i - 1][j] == '.':
                        dsu.join(line(i - 1, j), line(i, j))
    s = set()
    for i in range(n):
        for j in range(m):
            tmp = dsu.find(line(i, j))
            if tmp not in (-1, dsu.find(ocean)):
                s.add(tmp)
    s = [(dsu.find(i), dsu.size[dsu.find(i)]) for i in s]
    s.sort(key=lambda x: x[1])
    if len(s) == k:
        print(0)
        print(*(''.join(r) for r in g), sep='\n')
        return
    s = s[:len(s) - k]
    ans = sum((x[1] for x in s))
    s = {x[0] for x in s}
    for i in range(n):
        for j in range(m):
            if dsu.find(line(i, j)) in s:
                g[i][j] = '*'
    print(ans)
    print(*(''.join(r) for r in g), sep='\n')


main()
