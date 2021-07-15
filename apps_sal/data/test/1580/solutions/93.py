# UnionFind: https://note.nkmk.me/python-union-find/
class UnionFind():
    def __init__(self, n):
        self.n = n
        self.root = [-1] * (n + 1)
        
    def find(self, x):
        if self.root[x] < 0:
            return x
        else:
            self.root[x] = self.find(self.root[x])
            return self.root[x]
    
    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return False
        if self.root[x] > self.root[y]:
            x, y = y, x
        self.root[x] += self.root[y]
        self.root[y] = x
        
    def is_same(self, x, y):
        return self.find(x) == self.find(y)
    
    def size(self, x):
        return -self.root[self.find(x)]

n, m = map(int, input().split())
cards = UnionFind(n)
for i in range(m):
    x, y, z = map(int, input().split())
    cards.unite(x, y)
print(sum(cards.find(i) == i for i in range(1, n + 1)))
