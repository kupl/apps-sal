n, m = map(int, input().split())
edge = [list(map(int, input().split())) for _ in range(m)]
edge = sorted(edge, key=lambda x: x[2])


class Union:
    def __init__(self, n):
        self.p = [i for i in range(n + 1)]
        self.rank = [0] * (n + 1)

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x != y:
            if self.rank[x] < self.rank[y]:
                self.p[x] = y
                self.rank[y] += self.rank[x]
            else:
                self.p[y] = x
                self.rank[x] += self.rank[y]


cnt = 0
used = [0] * m
l, r = 0, 1
U = Union(n)

while l < m:
    try:
        while r < m and edge[r][2] == edge[l][2]:
            r += 1
    except:
        print('bl1')

    try:
        for i in range(l, r):
            u, v, w = edge[i]
            if U.find(u) == U.find(v):
                used[i] = 1
    except:
        print('bl2')

    try:
        for i in range(l, r):
            if used[i] == 1:
                continue

            u, v, w = edge[i]
            if U.find(u) == U.find(v):
                cnt += 1
            else:
                U.union(u, v)
    except:
        print('bl3')
        print(u, v)
        print(U.find(u))
        print(U.find(v))

    l = r
    r = l + 1

print(cnt)
