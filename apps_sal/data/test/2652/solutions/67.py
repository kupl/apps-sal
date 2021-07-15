#UnionFind木とそれを利用したクラスカル法
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

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def nums(self,x):
        return abs(self.parents[self.find(x)])

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


N = int(input())
A = [list(map(int, input().split()))+[i] for i in range(N)]
edge = []
A.sort()
for i in range(N-1):
    w = A[i+1][0]-A[i][0]
    edge.append((w,A[i][2],A[i+1][2]))
A.sort(key=lambda x:x[1])
for i in range(N-1):
    w = A[i+1][1]-A[i][1]
    edge.append((w,A[i][2],A[i+1][2]))

edge.sort()

uf = UnionFind(N)
ans = 0
for i in range(len(edge)):
    u,x,y = edge[i]
    if not uf.same(x,y):
        uf.union(x,y)
        ans += u
print(ans)
