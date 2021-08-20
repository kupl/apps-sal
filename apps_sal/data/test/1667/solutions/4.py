class Union:

    def __init__(self, n):
        self.p = {i: i for i in range(n)}
        self.rank = {i: 1 for i in range(n)}

    def find(self, x):
        if x < 0:
            return x
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        if x < 0 or y < 0:
            return
        x = self.find(x)
        y = self.find(y)
        if x != y:
            if self.rank[x] < self.rank[y]:
                self.p[x] = y
                self.rank[y] += self.rank[x]
            else:
                self.p[y] = x
                self.rank[x] += self.rank[y]


def add(d, key, val):
    if key not in d:
        d[key] = 0
    d[key] += val
    if d[key] == 0:
        del d[key]


def update(i, used, d, u):
    used[i] = True
    add(d, 1, 1)
    if i - 1 >= 0 and used[i - 1] == True:
        par_1 = u.find(i)
        par_2 = u.find(i - 1)
        size_1 = u.rank[par_1]
        size_2 = u.rank[par_2]
        add(d, size_1, -1)
        add(d, size_2, -1)
        add(d, size_1 + size_2, 1)
        u.union(par_1, par_2)
    if i + 1 < n and used[i + 1] == True:
        par_1 = u.find(i)
        par_2 = u.find(i + 1)
        size_1 = u.rank[par_1]
        size_2 = u.rank[par_2]
        add(d, size_1, -1)
        add(d, size_2, -1)
        add(d, size_1 + size_2, 1)
        u.union(par_1, par_2)


n = int(input())
a_ = list(map(int, input().split()))
a = [(i, x) for (i, x) in enumerate(a_)]
a = sorted(a, key=lambda x: x[1])
u = Union(n)
d = {}
used = [False] * n
ans = -1
max_length = -1
for (index, val) in a:
    update(index, used, d, u)
    if len(d) == 1:
        len_ = list(d.values())[0]
        if max_length < len_:
            max_length = len_
            ans = val + 1
print(ans)
