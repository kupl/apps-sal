class UnionFind:

    def __init__(self, n):
        self.table = [-1] * n

    def _root(self, x):
        if self.table[x] < 0:
            return x
        else:
            self.table[x] = self._root(self.table[x])
            return self.table[x]

    def find(self, x, y):
        return self._root(x) == self._root(y)

    def union(self, x, y):
        r1 = self._root(x)
        r2 = self._root(y)
        if r1 == r2:
            return
        d1 = self.table[r1]
        d2 = self.table[r2]
        if d1 <= d2:
            self.table[r2] = r1
            if d1 == d2:
                self.table[r1] -= 1
        else:
            self.table[r1] = r2


def __starting_point():
    (n, k, l) = map(int, input().split())
    pq = UnionFind(n + 1)
    rs = UnionFind(n + 1)
    for i in range(k):
        (p, q) = map(int, input().split())
        pq.union(p, q)
    for i in range(l):
        (r, s) = map(int, input().split())
        rs.union(r, s)
    sameroot = []
    for i in range(1, n + 1):
        sameroot.append([pq._root(i), rs._root(i), i])
    sameroot.sort()
    sameroot.append([0, 0, n + 1])
    cnt = [0] * (n + 1)
    (bx, by) = (0, 0)
    samelist = []
    for (x, y, i) in sameroot:
        if bx == x and by == y:
            samelist.append(i)
        else:
            k = len(samelist)
            if k > 0:
                for j in samelist:
                    cnt[j] = k
            samelist = [i]
            (bx, by) = (x, y)
    print(' '.join(map(str, cnt[1:])))


__starting_point()
