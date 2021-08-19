import sys
sys.setrecursionlimit(10 ** 7)


class TreeNode:

    def __init__(self, num):
        self.num = num
        self.vertexs = []
        self.color = None

    def set_color(self, color):
        self.color = color


class Tree:

    def __init__(self, N):
        self.nodes = [TreeNode(i) for i in range(N)]

    def set_vertex(self, u, v, w):
        self.nodes[u - 1].vertexs.append((v - 1, w))
        self.nodes[v - 1].vertexs.append((u - 1, w))

    def set_color(self):
        self.nodes[0].set_color(0)

        def set_color(node, prev_node):
            for (n, w) in node.vertexs:
                if n != prev_node.num:
                    continue
                if w % 2 == 0:
                    node.set_color(prev_node.color)
                else:
                    new_color = abs(prev_node.color - 1)
                    node.set_color(new_color)
        self.do_and_next(0, -1, set_color)

    def print_tree_num(self):
        for (i, node) in enumerate(self.nodes):
            print(i, node.vertexs, node.color)

    def print_tree_deep(self):

        def print_color(x, p):
            return print(x.color)
        self.do_and_next(0, -1, print_color)

    def do_and_next(self, node_num, prev_node_num, f):
        f(self.nodes[node_num], self.nodes[prev_node_num])
        for (n, w) in self.nodes[node_num].vertexs:
            if n == prev_node_num:
                continue
            self.do_and_next(n, node_num, f)

    def print_color(self):
        for node in self.nodes:
            print(node.color)


N = int(input())
tree = Tree(N)
for _ in range(N - 1):
    (u, v, w) = map(int, input().split())
    tree.set_vertex(u, v, w)
tree.set_color()
tree.print_color()
