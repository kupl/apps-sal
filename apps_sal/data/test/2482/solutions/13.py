(N, M, L) = [int(s) for s in input().split()]
parent_road = list(range(N))
parent_train = list(range(N))
rank_road = [0] * N
rank_train = [0] * N


class UnionFind:

    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * N

    def find(self, x):
        if x == self.parent[x]:
            return x
        else:
            self.parent[x] = self.find(self.parent[x])
            return self.parent[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)
        if self.rank[x] < self.rank[y]:
            self.parent[x] = y
        else:
            self.parent[y] = x
            if self.rank[x] == self.rank[y]:
                self.rank[x] += 1


edge_road = [[int(s) - 1 for s in input().split()] for _ in range(M)]
edge_train = [[int(s) - 1 for s in input().split()] for _ in range(L)]
group_road = UnionFind(N)
group_train = UnionFind(N)
for (x, y) in edge_road:
    group_road.union(x, y)
for (x, y) in edge_train:
    group_train.union(x, y)
group_count = {}
group_list = []
for i in range(N):
    gr = group_road.find(i)
    gt = group_train.find(i)
    group_list.append((gr, gt))
    if (gr, gt) in list(group_count.keys()):
        group_count[gr, gt] += 1
    else:
        group_count[gr, gt] = 1
print(' '.join([str(group_count[g]) for g in group_list]))
