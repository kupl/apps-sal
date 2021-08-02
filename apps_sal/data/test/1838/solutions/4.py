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


n, m, q = map(int, input().split())
listW = input().split()
dic = {w: i for i, w in enumerate(listW)}
u = Union(n)
opposite = {i: -(i + 1) for i in range(n)}

for i in range(m):
    t, s1, s2 = input().split()
    x = u.find(dic[s1])
    y = u.find(dic[s2])

    if t == '1':
        if opposite[x] == y:
            print('NO')
        else:
            print('YES')
            if x != y:
                ox = opposite[x]
                oy = opposite[y]
                op = max(ox, oy)

                u.union(x, y)
                u.union(ox, oy)

                op = u.find(op)
                p = u.find(x)

                if op > 0:
                    opposite[p] = op
                    opposite[op] = p

    else:
        if x == y:
            print('NO')
        else:
            print('YES')
            if opposite[x] != y:
                u.union(y, opposite[x])
                u.union(x, opposite[y])
                x = u.find(x)
                y = u.find(y)
                opposite[x] = y
                opposite[y] = x

for _ in range(q):
    s1, s2 = input().split()
    id1, id2 = u.find(dic[s1]), u.find(dic[s2])

    if id1 == id2:
        print(1)
    elif opposite[id1] == id2:
        print(2)
    else:
        print(3)
