def INT(): return int(input())


def INTM(): return map(int, input().split())
def STRM(): return map(str, input().split())
def STR(): return str(input())


def LIST(): return list(map(int, input().split()))
def LISTS(): return list(map(str, input().split()))


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


def do():
    n, m, k = INTM()
    uf = UnionFind(n)
    fri = [[] for i in range(n)]
    blo = [[] for i in range(n)]
    for i in range(m):
        a, b = INTM()
        a -= 1
        b -= 1
        fri[a].append(b)
        fri[b].append(a)
        uf.union(a, b)
    for i in range(k):
        c, d = INTM()
        c -= 1
        d -= 1
        blo[c].append(d)
        blo[d].append(c)

    ans = []

    for i in range(n):
        blos = 0
        for j in blo[i]:
            if uf.same(i, j):
                blos += 1

        ans.append(uf.size(i) - 1 - len(fri[i]) - blos)

    print(*ans)


def __starting_point():
    do()


__starting_point()
