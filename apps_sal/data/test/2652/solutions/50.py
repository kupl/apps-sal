from itertools import permutations


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


n = int(input())
list_XY = []
list_CO = []
for i in range(n):
    x, y = map(int, input().split())
    list_XY.append([x, y, i])

list_XY.sort(key=lambda x: x[0])
for i in range(n - 1):
    list_CO.append([list_XY[i][2], list_XY[i + 1][2], abs(list_XY[i][0] - list_XY[i + 1][0])])

list_XY.sort(key=lambda x: x[1])
for i in range(n - 1):
    list_CO.append([list_XY[i][2], list_XY[i + 1][2], abs(list_XY[i][1] - list_XY[i + 1][1])])

list_CO.sort(key=lambda x: x[2])
uf = UnionFind(n)
ans = 0

for i, j, cost in list_CO:
    if not uf.same(i, j):
        uf.union(i, j)
        ans += cost
    if uf.size(0) == n:
        break

print(ans)
