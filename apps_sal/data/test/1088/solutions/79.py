from math import factorial
MOD = 998244353
N, K = list(map(int, input().split()))
field = [list(map(int, input().split())) for i in range(N)]


class Union_Find:
    def __init__(self, N):
        self.parent = [-1] * N
        self.rank = [0] * N
        self.group_count = N
        self.N = N

    def find(self, x):
        if self.parent[x] < 0:
            return x

        par = self.find(self.parent[x])
        self.parent[x] = par
        return par

    def unite(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.rank[x] == self.rank[y]:
            self.parent[x] += self.parent[y]
            self.parent[y] = x
            self.rank[x] += 1

        elif self.rank[x] > self.rank[y]:
            self.parent[x] += self.parent[y]
            self.parent[y] = x
        else:
            self.parent[y] += self.parent[x]
            self.parent[x] = y

        self.group_count -= 1

    def samep(self, x, y):
        return self.find(x) == self.find(y)

    def get_group_member_list(self, x):
        x = self.find(x)
        return [i for i in range(self.N) if self.find(i) == x]

    def get_group_member_count(self, x):
        x = self.find(x)
        return -self.parent[x]

    def get_all_groups(self):
        return {idx: -n for idx, n in enumerate(self.parent) if n < 0}


hg = Union_Find(N)
for i in range(N - 1):
    h1 = field[i]
    for j in range(i, N):
        h2 = field[j]
        if all([True if x + y <= K else False for x, y in zip(h1, h2)]):
            hg.unite(i, j)

vg = Union_Find(N)
rotated = list(zip(*field))
for i in range(N - 1):
    v1 = rotated[i]
    for j in range(i, N):
        v2 = rotated[j]
        if all([True if x + y <= K else False for x, y in zip(v1, v2)]):
            vg.unite(i, j)

result = 1
for value in list(hg.get_all_groups().values()):
    result *= factorial(value)
    result %= MOD

for value in list(vg.get_all_groups().values()):
    result *= factorial(value)
    result %= MOD

print(result)
