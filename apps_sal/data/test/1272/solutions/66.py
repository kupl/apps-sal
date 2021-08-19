import sys
input = sys.stdin.readline


class UnionFind:
    def __init__(self, size):
        self.parent = [-1] * size
        self.rank = [1] * size
        self.groups = size

    def get_root(self, node):
        parent = self.parent[node]
        if parent == -1:
            root = node
        else:
            root = self.get_root(parent)
            self.parent[node] = root  # 同じnodeへの2回目以降のget_rootを高速にするために、直接rootに繋いでおく
        return root

    def in_same_group(self, node1, node2):
        root1 = self.get_root(node1)
        root2 = self.get_root(node2)
        return root1 == root2

    def unite(self, node1, node2):
        if self.in_same_group(node1, node2):
            return
        main_root = self.get_root(node1)
        sub_root = self.get_root(node2)
        if self.rank[main_root] < self.rank[sub_root]:  # rankの大きい方をmain_rootにする
            main_root, sub_root = sub_root, main_root

        self.parent[sub_root] = main_root
        self.rank[main_root] += self.rank[sub_root]
        self.groups -= 1


def main():
    n, m = map(int, input().split())
    bridges = [list(map(int, input().split())) for _ in range(m)]
    uf = UnionFind(n)
    inconvenience = n * (n - 1) // 2
    ans = [inconvenience]

    for a, b in bridges[::-1]:
        if uf.in_same_group(a - 1, b - 1):
            ans.append(inconvenience)
            continue
        root1 = uf.get_root(a - 1)
        root2 = uf.get_root(b - 1)
        pattern = uf.rank[root1] * uf.rank[root2]
        inconvenience -= pattern
        ans.append(inconvenience)
        uf.unite(root1, root2)
    ans.pop()
    print(*ans[::-1], sep="\n")


def __starting_point():
    main()


__starting_point()
