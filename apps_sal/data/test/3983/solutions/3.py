class UnionFind:
    def __init__(self, n):
        self.table = [-1] * n

    def _root(self, x):
        stack = []
        tbl = self.table
        while tbl[x] >= 0:
            stack.append(x)
            x = tbl[x]
        for y in stack:
            tbl[y] = x
        return x

    def find(self, x, y):
        return self._root(x) == self._root(y)

    def unite(self, x, y):
        r1 = self._root(x)
        r2 = self._root(y)
        if r1 == r2:
            return
        d1 = self.table[r1]
        d2 = self.table[r2]
        if d1 <= d2:
            self.table[r2] = r1
            self.table[r1] += d2
        else:
            self.table[r1] = r2
            self.table[r2] += d1

    def get_size(self, x):
        return -self.table[self._root(x)]


t = int(input())
buf = []
for _ in range(t):
    n, m = list(map(int, input().split()))

    if n % 2 == 1:
        if (n * (n - 1) // 2 - m) & 1:
            buf.append('First')
        else:
            buf.append('Second')
        for _ in range(m):
            input()
        continue

    uft = UnionFind(n)
    for _ in range(m):
        a, b = list(map(int, input().split()))
        a -= 1
        b -= 1
        uft.unite(a, b)

    s = uft.get_size(0)
    t = uft.get_size(n - 1)

    if (s & 1) ^ (t & 1):
        buf.append('First')
    elif (n * (n - 1) // 2 - m) & 1:
        if s & 1 == 0:
            buf.append('First')
        else:
            buf.append('Second')
    else:
        if s & 1 == 0:
            buf.append('Second')
        else:
            buf.append('First')

print(('\n'.join(buf)))
