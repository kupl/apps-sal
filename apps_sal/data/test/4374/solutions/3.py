import sys
sys.setrecursionlimit(10000)


class Tree:

    def __init__(self, nodes):
        self.root = None


class Node:

    def __init__(self, val):
        self.parent = None
        self.val = val
        self.children = []

    def add(self, child):
        self.children.append(child)

    def get_max_dist(self, parent, dist):
        max_dist = dist
        for i in self.children:
            if i != parent:
                d = i.get_max_dist(self, dist + 1)
                if max_dist < d:
                    max_dist = d
        return max_dist

    def get_dist(self):
        return self.get_max_dist(self, 0)

    def get_count_ch(self, parent):
        count = len(self.children)
        for i in self.children:
            if i != parent:
                count += i.get_count_ch(self) - 1
        return count

    def calc_child(self):
        return (self.get_count_ch(None), len(self.children), self.val)


class Forest:

    def __init__(self, count):
        self.nodes = []
        self.count = count
        self.set_nodes = set()

    def build(self):
        roots = []
        max_dist = []
        list_root = []
        for i in self.nodes:
            tree = list([x.get_dist() for x in i])
            ma = max(tree)
            max_dist.append(ma)
            m = i[tree.index(min(tree))]
            roots.append(m)
        if len(roots) > 1:
            ind = max_dist.index(max(max_dist))
            if len(roots) > 1 and ind != 0:
                (roots[0], roots[ind]) = (roots[ind], roots[0])
        s = set()
        for i in self.nodes:
            for j in i:
                s.add(j.val)
        r = list(set(range(1, n + 1)) - s)
        if len(roots) > 0:
            for i in range(1, len(roots)):
                self.add(roots[0].val, roots[i].val)
                list_root.append((roots[0].val, roots[i].val))
            for i in r:
                self.add(roots[0].val, i)
                list_root.append((roots[0].val, i))
        elif len(r) == 1:
            print(0)
            return
        elif len(r) > 1:
            for i in range(1, len(r)):
                self.add(r[0], r[i])
                list_root.append((r[0], r[i]))
        distances = []
        for i in self.nodes[0]:
            dist = i.get_dist()
            distances.append(dist)
        print(max(distances))
        for i in list_root:
            print(*i)

    def add(self, v, u):
        self.set_nodes.add(v)
        self.set_nodes.add(u)
        (v_node, v_list) = self.find(v)
        (u_node, u_list) = self.find(u)
        if v_node == None and u_node == None:
            v_node = Node(v)
            u_node = Node(u)
            v_node.add(u_node)
            u_node.add(v_node)
            self.nodes.append([v_node, u_node])
        elif v_node != None and u_node != None and (v_list != u_list):
            v_node.add(u_node)
            u_node.add(v_node)
            v_list += u_list
            self.nodes.remove(u_list)
        elif v_node == None and u_node != None:
            v_node = Node(v)
            u_node.add(v_node)
            v_node.add(u_node)
            u_list.append(v_node)
        elif v_node != None and u_node == None:
            u_node = Node(u)
            v_node.add(u_node)
            u_node.add(v_node)
            v_list.append(u_node)

    def find(self, value):
        for i_list in self.nodes:
            for i in i_list:
                if i.val == value:
                    return (i, i_list)
        return (None, None)


(n, m) = list(map(int, input().split()))
f = Forest(n)
for i in range(m):
    (v, u) = list(map(int, input().split()))
    f.add(v, u)
f.build()
