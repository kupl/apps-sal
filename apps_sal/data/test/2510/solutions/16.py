class UnionFind:

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
            (x, y) = (y, x)
        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]


(N, M) = map(int, input().split())
union_find = UnionFind(N)
for _ in range(M):
    (A, B) = map(int, input().split())
    A -= 1
    B -= 1
    union_find.union(A, B)
answer = 0
for i in range(N):
    answer = max(answer, union_find.size(i))
print(answer)
