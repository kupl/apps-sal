class UnionFind:

    def __init__(self, n):
        self.n = n
        self.parents = [i for i in range(n)]
        self.ranks = [0 for _ in range(n)]

    def root(self, node):
        parent_node = self.parents[node]
        if parent_node == node:
            return node
        root_node = self.root(parent_node)
        self.parents[node] = root_node  # reduction
        return root_node

    def union(self, one_node, other_node):
        one_root = self.root(one_node)
        other_root = self.root(other_node)
        if one_root == other_root:
            return
        if self.ranks[one_root] < self.ranks[other_root]:
            self.parents[one_root] = other_root
        else:
            self.parents[other_root] = one_root
            if self.ranks[one_root] == self.ranks[other_root]:
                self.ranks[one_root] += 1


def main():
    N, M = list(map(int, input().split(' ')))
    tree = UnionFind(N)
    for _ in range(M):
        x, y, _ = list(map(int, input().split(' ')))
        tree.union(x - 1, y - 1)
    roots = list(map(lambda n: tree.root(n), range(N)))
    print(len(set(roots)))


def __starting_point():
    main()
__starting_point()
