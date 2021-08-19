class UnionFind(object):

    def __init__(self, n):
        self.root = [i for i in range(n)]
        self.size = [1 for i in range(n)]

    def find(self, x):
        if self.root[x] == x:
            return x
        self.root[x] = self.find(self.root[x])
        return self.root[x]

    def union(self, x, y):
        (x, y) = (self.find(x), self.find(y))
        if x == y:
            return False
        if self.size[x] < self.size[y]:
            (x, y) = (y, x)
        self.size[x] += self.size[y]
        self.root[y] = x
        return True


def main():
    (n, m) = list(map(int, input().split()))
    edge_list = []
    for _ in range(m):
        edge_list.append(list(map(int, input().split())))
    union_find = UnionFind(n + 1)
    edge_list.sort(key=lambda x: x[2])
    p1 = ret = 0
    while p1 < m:
        p2 = p1
        while p2 < m and edge_list[p1][2] == edge_list[p2][2]:
            p2 += 1
        avail = used = 0
        for i in range(p1, p2):
            if union_find.find(edge_list[i][0]) != union_find.find(edge_list[i][1]):
                avail += 1
        for i in range(p1, p2):
            if union_find.union(edge_list[i][0], edge_list[i][1]):
                used += 1
        ret += avail - used
        p1 = p2
    print(ret)


def __starting_point():
    main()


__starting_point()
