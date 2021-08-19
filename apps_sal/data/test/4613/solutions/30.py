class node:

    def __init__(self, id):
        self.id = id
        self.root = self

    def findRoot(self):
        if self == self.root:
            return self
        else:
            self.root = self.root.findRoot()
            return self.root

    def resetRoot(self):
        self.root = self


class Tree:

    def __init__(self, num):
        self.nodes = {i: node(i) for i in range(num)}

    def union(self, one, other):
        root1 = one.findRoot()
        root2 = other.findRoot()
        root1.root = root2.root = self.nodes[min(root1.id, root2.id)]

    def resetTree(self):
        for n in self.nodes.values():
            n.resetRoot()

    def makeTree(self, Edge):
        self.edge = Edge
        for (x, y) in Edge:
            self.union(self.nodes[x - 1], self.nodes[y - 1])


def main():
    with open(0) as f:
        (N, M) = map(int, f.readline().split())
        Edge = [tuple(map(int, line.split())) for line in f.readlines()]
    tree = Tree(N)
    ans = 0
    for i in range(M):
        edge = [v for v in Edge if v != Edge[i]]
        tree.makeTree(edge)
        if any((x.findRoot().id != 0 for x in tree.nodes.values())):
            ans += 1
        tree.resetTree()
    print(ans)


def __starting_point():
    main()


__starting_point()
