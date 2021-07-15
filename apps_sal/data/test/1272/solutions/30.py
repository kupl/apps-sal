import sys
breadline = sys.stdin.buffer.readline
bread = sys.stdin.buffer.read
readline = sys.stdin.readline
read = sys.stdin.read
sys.setrecursionlimit(10 ** 7)
def getnum(t=int): return t(breadline())
def numline(t=int): return map(t, breadline().split())
def numread(t=int): return map(t, bread().split())
def getstr(): return readline().strip()
def strline(): return readline().strip().split()
def strread(): return read().strip().split()

class UnionFind:
    def __init__(self, n):
        '''self.parents: the size of tree(as negative value)'''
        self.n = n
        self.parents = [-1] * n
        self.ROOTS = set(list(range(n)))
        self.n_connections = 0

    def find(self, x):
        '''Return parent node'''
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def _connect(self,x): return x * (x-1) // 2

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if x == y:
            return
        if self.parents[x] > self.parents[y]:
            x,y = y,x
        self.n_connections -= self._connect(-self.parents[x]) + self._connect(-self.parents[y])
        self.parents[x] += self.parents[y]
        self.parents[y] = x
        self.ROOTS.remove(y)
        self.n_connections += self._connect(-self.parents[x])


    def size(self, x):
        parent = self.find(x)
        return -self.parents[parent]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        '''return the number in the group'''
        parent = self.find(x)
        return [i for i in range(self.n) if self.find(i) == parent]

    def group_count(self): return len(self.ROOTS)

    def all_roots(self): return self.ROOTS



def main():
    N,M = numline()
    AB = []
    for i in range(M):
        a,b = numline()
        AB.append((a-1, b-1))
    tr = UnionFind(N)

    BASE = N * (N-1) // 2
    ans = [BASE]
    for i in range(M-1, -1, -1):
        a,b = AB[i]
        tr.union(a,b)
        ans.append(BASE - tr.n_connections)

    for a in ans[-2::-1]:
        print(a)


def __starting_point():
    main()
__starting_point()
