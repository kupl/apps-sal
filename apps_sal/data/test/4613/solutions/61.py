class UnionFind:
    def __init__(self, n):
        self._n = n
        self._table = [-1]*n

    def _root(self, x):
        stack = []
        while self._table[x] >= 0:
            stack.append(x)
            x = self._table[x]
        for y in stack:
            self._table[y] = x
        return x
    
    def unite(self, x, y):
        x, y = self._root(x), self._root(y)
        if x == y:
            return
        if x > y:
            x, y = y, x
        self._table[x] += self._table[y]
        self._table[y] = x
    
    def same(self, x, y):
        return self._root(x) == self._root(y)

    def count_members(self, x):
        return -self._table[self._root(x)]
    
    def count_groups(self):
        return len({self._root(i) for i in range(self._n)})
    
    def __str__(self):
        return str([self._root(i) for i in range(self._n)])
    
    def __repr__(self):           
        return repr([self._root(i) for i in range(self._n)])

n, m, *AB = map(int, open(0).read().split())
ans = 0
for i in range(m):
    uf = UnionFind(n)
    for j, (a, b) in enumerate(zip(AB[::2], AB[1::2])):
        if i == j:
            continue
        uf.unite(a-1, b-1)
    ans += uf.count_groups() != 1
print(ans)
