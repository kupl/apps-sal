n,m=map(int,input().split())
class UnionFind:
    #def   -> foo=UnionFind(n,1)  <- 1-based index, default is 0
    #method -> foo.hoge(huga)
    __slots__ = ["_size", "_first_idx", "_parents"]
    def __init__(self, size: int, first_index: int = 0) -> None:
        self._size = size
        self._first_idx = first_index
        self._parents = [-1] * (size + first_index)
    def find(self, x: int) -> int:
        if self._parents[x] < 0:
            return x
        self._parents[x] = self.find(self._parents[x])
        return self._parents[x]
    def same(self, x: int, y: int) -> bool:
        return self.find(x) == self.find(y)
    def unite(self, x: int, y: int) -> bool:
        x, y = self.find(x), self.find(y)
        if x == y:
            return False
        if self._parents[x] > self._parents[y]:
            x, y = y, x
        self._parents[x] += self._parents[y]
        self._parents[y] = x
        return True
    def size(self, x: int) -> int:
        return -self._parents[self.find(x)]
    def group_count(self) ->int:
        return sum([1 for i in  self._parents if i<0])-self._first_idx
    def connected(self) ->bool:
        return self._parents[self.find(self._first_idx)]==-self._size

uf=UnionFind(n,1)
for i in range(m):
    x,y,z=map(int,input().split())
    uf.unite(x,y)
print(uf.group_count())
