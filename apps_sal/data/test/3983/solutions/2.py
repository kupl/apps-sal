import sys


class UnionFind:

    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def root(self, x):
        while self.parent[x] != x:
            self.parent[x] = self.parent[self.parent[x]]
            x = self.parent[x]
        return x

    def merge(self, x, y):
        (x, y) = (self.root(x), self.root(y))
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            (x, y) = (y, x)
        self.size[x] += self.size[y]
        self.parent[y] = x
        return True

    def issame(self, x, y):
        return self.root(x) == self.root(y)

    def getsize(self, x):
        return self.size[self.root(x)]


readline = sys.stdin.readline
read = sys.stdin.read


def solve():
    (n, m) = list(map(int, readline().split()))
    UF = UnionFind(n)
    for _ in range(m):
        (a, b) = list(map(int, readline().split()))
        UF.merge(a - 1, b - 1)
    s1 = UF.getsize(0) % 2
    s2 = UF.getsize(n - 1) % 2
    if n % 4 == 0:
        if s1 == s2 == m % 2:
            return 1
        return 0
    elif n % 4 == 2:
        if s1 == s2 == 1 - m % 2:
            return 1
        return 0
    elif n % 4 == 1:
        if m % 2 == 0:
            return 1
        else:
            return 0
    elif n % 4 == 3:
        if m % 2 == 0:
            return 0
        else:
            return 1


ans = ['First', 'Second']
(T,) = list(map(int, readline().split()))
for i in range(T):
    x = solve()
    print(ans[x])
