from collections import defaultdict


class UnionFind:

    def __init__(self, n):
        # * Access m-th node by index `m`, not `m - 1`.
        self.parents = [i for i in range(n + 1)]
        self.ranks = [0 for _ in range(n + 1)]

    def find_root(self, node):
        parent_node = self.parents[node]
        if parent_node == node:
            return node
        else:
            root_node = self.find_root(parent_node)
            self.parents[node] = root_node  # reduction
            return root_node

    def union(self, one, other):
        one_root = self.find_root(one)
        other_root = self.find_root(other)
        if one_root == other_root:
            return
        if self.ranks[one_root] < self.ranks[other_root]:
            self.parents[one_root] = other_root
        else:
            self.parents[other_root] = one_root
            if self.ranks[one_root] == self.ranks[other_root]:
                self.ranks[one_root] += 1

    def is_same_group(self, one, other):
        one_root = self.find_root(one)
        other_root = self.find_root(other)
        return one_root == other_root


def main():
    N, K, L = list(map(int, input().split(' ')))
    road_tree = UnionFind(N)
    for _ in range(K):
        p, q = list(map(int, input().split(' ')))
        road_tree.union(p, q)
    train_tree = UnionFind(N)
    for _ in range(L):
        r, s = list(map(int, input().split(' ')))
        train_tree.union(r, s)
    # Calculate groups
    group_count = defaultdict(int)
    group_list = list()
    for node in range(1, N + 1):
        group = (road_tree.find_root(node), train_tree.find_root(node))
        group_count[group] += 1
        group_list.append(group)
    answer = ' '.join(list(map(
        lambda g: str(group_count[g]),
        group_list
    )))
    print(answer)


def __starting_point():
    main()
__starting_point()
