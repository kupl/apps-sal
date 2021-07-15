
import itertools,math
from collections import defaultdict
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
        group_members = defaultdict(list)
        for member in range(self.n):
            group_members[self.find(member)].append(member)
        return group_members

    def __str__(self):
        return '\n'.join(f'{r}: {m}' for r, m in list(self.all_group_members().items()))
n,k = list(map(int,input().split()))
a = [list(map(int,input().split())) for i in range(n)]
a_row = []
a_column = []
for i in itertools.combinations(list(range(n)),2):
    for j in range(n):
        if a[i[0]][j] + a[i[1]][j] > k:
            break
        if j == n - 1:
            a_row.append(i)
    for j in range(n):
        if a[j][i[0]] + a[j][i[1]] > k:
            break
        if j == n - 1:
            a_column.append(i)
uf_row = UnionFind(n)
uf_column = UnionFind(n)
for i in a_row:
    uf_row.union(i[0],i[1])
for i in a_column:
    uf_column.union(i[0],i[1])
ans = 1
for i in list(uf_row.all_group_members().values()):
    ans = ans * math.factorial(len(i)) % 998244353
for i in list(uf_column.all_group_members().values()):
    ans = ans * math.factorial(len(i)) % 998244353
print(ans)

