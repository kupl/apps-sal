(n, m) = map(int, input().split())
a = []
for i in range(m):
    a.append(list(map(int, input().split())))
b = [set([]) for i in range(n)]
for i in range(n):
    for j in range(m):
        ya = a[j][i]
        if i == n - 1:
            b[ya - 1].add(100000000)
        else:
            b[ya - 1].add(a[j][i + 1])


class UnionFind:

    def __init__(self, size):
        self.table = [-1 for _ in range(size)]

    def find(self, x):
        while self.table[x] >= 0:
            x = self.table[x]
        return x

    def union(self, x, y):
        s1 = self.find(x)
        s2 = self.find(y)
        if s1 != s2:
            if self.table[s1] != self.table[s2]:
                if self.table[s1] < self.table[s2]:
                    self.table[s2] = s1
                else:
                    self.table[s1] = s2
            else:
                self.table[s1] += -1
                self.table[s2] = s1
        return


UN = UnionFind(n)
for i in range(n):
    if len(b[i]) == 1 and list(b[i])[0] != 100000000:
        UN.union(i, list(b[i])[0] - 1)
d = [0] * n
for i in range(n):
    d[UN.find(i)] += 1
ans = 0
for i in range(n):
    ans += (d[i] - 1) * d[i] // 2
print(ans + n)
