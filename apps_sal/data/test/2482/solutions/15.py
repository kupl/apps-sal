from collections import Counter


class UnionFind:

    def __init__(self, node):
        self.parent = [-1 for _ in range(node)]
        self.node = node

    def find(self, target):
        if self.parent[target] < 0:
            return target
        else:
            self.parent[target] = self.find(self.parent[target])
            return self.parent[target]

    def is_same(self, x, y):
        return self.find(x) == self.find(y)

    def union(self, x, y):
        root_x = self.find(x)
        root_y = self.find(y)
        if root_x == root_y:
            return
        if self.parent[root_x] > self.parent[root_y]:
            (root_x, root_y) = (root_y, root_x)
        self.parent[root_x] += self.parent[root_y]
        self.parent[root_y] = root_x

    def get_size(self, x):
        return -self.parent[self.find(x)]

    def members(self, x, is_set=False):
        root = self.find(x)
        res = [i for i in range(self.node) if self.find(i) == root]
        if is_set:
            return set(res)
        return res

    def all_root(self):
        return [idx for (idx, val) in enumerate(self.parent) if val < 0]


def main():
    (cities, roads, railroads) = list(map(int, input().split()))
    uf_road = UnionFind(cities)
    uf_train = UnionFind(cities)
    for _ in range(roads):
        (p, q) = [int(x) - 1 for x in input().split()]
        uf_road.union(p, q)
    for _ in range(railroads):
        (r, s) = [int(x) - 1 for x in input().split()]
        uf_train.union(r, s)
    each_pair = []
    for i in range(cities):
        each_pair.append(tuple([uf_road.find(i), uf_train.find(i)]))
    pair_count = dict(Counter(each_pair))
    answer = [pair_count[each_pair[i]] for i in range(cities)]
    print(' '.join(map(str, answer)))


def __starting_point():
    main()


__starting_point()
