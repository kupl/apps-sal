import sys
import numpy as np


def inputs(func=lambda x: x, sep=None, maxsplit=-1):
    return list(map(func, sys.stdin.readline().split(sep=sep, maxsplit=maxsplit)))


def input_row(n: int, type=np.int, *args, **kwargs):
    return np.fromiter(inputs(type, *args, **kwargs), dtype=type)


def input_2d(nrows: int, ncols: int, type=np.int, *args, **kwargs):
    data = np.zeros((nrows, ncols), dtype=type)
    for i in range(nrows):
        data[i, :] = input_row(ncols, type, *args, **kwargs)
    return data


class IntAddition(object):
    """整数の加法"""

    def operate(self, x, y):
        return x + y

    @property
    def identity(self):
        return 0

    def cancel(self, x, y):
        return x - y

    def invert(self, x):
        return -x

    def accumulate(self, x, count):
        return x * count


class UnionFindNode(object):
    __slots__ = ['parent_index', 'size', 'difference_from_parent']

    def __init__(self, index: int, potential_identity):
        self.parent_index = index
        self.size = 1
        self.difference_from_parent = potential_identity


class UnionFind(object):
    """重み付きUnion-Find木"""

    def __init__(self, num_nodes=0, potential_abelian=IntAddition()):
        self.nodes = []
        self.op = potential_abelian
        self.extend(num_nodes)

    def append(self):
        self.nodes.append(UnionFindNode(len(self.nodes), self.op.identity))

    def extend(self, num_nodes):
        self.nodes.extend((UnionFindNode(i, self.op.identity) for i in range(num_nodes)))

    def root(self, index: int):
        x = self.nodes[index]
        while x.parent_index != index:
            parent = self.nodes[x.parent_index]
            x.difference_from_parent = self.op.operate(x.difference_from_parent, parent.difference_from_parent)
            index = x.parent_index = parent.parent_index
            x = self.nodes[index]
        return index

    def difference_from_root_to(self, index: int):
        x = self.nodes[index]
        potential = x.difference_from_parent
        while x.parent_index != index:
            parent = self.nodes[x.parent_index]
            potential = self.op.operate(potential, parent.difference_from_parent)
            index = x.parent_index
            x = self.nodes[index]
        return potential

    def size(self, index: int):
        return self.nodes[self.root(index)].size

    def difference(self, x, y):
        if not self.issame(x, y):
            raise RuntimeError('x と y は同じ集合に属していません。')
        return self.op.cancel(self.difference_from_root_to(y), self.difference_from_root_to(x))

    def unite(self, x, y, difference=None) -> bool:
        if difference is None:
            difference = self.op.identity
        (x, px) = (self.root(x), self.difference_from_root_to(x))
        (y, py) = (self.root(y), self.difference_from_root_to(y))
        if x == y:
            return difference == self.op.cancel(py, px)
        difference = self.op.cancel(difference, py)
        difference = self.op.operate(difference, px)
        if self.size(x) < self.size(y):
            (x, y) = (y, x)
            difference = self.op.invert(difference)
        x_node = self.nodes[x]
        y_node = self.nodes[y]
        x_node.size += y_node.size
        y_node.parent_index = x
        y_node.difference_from_parent = difference
        return True

    def issame(self, x, y):
        return self.root(x) == self.root(y)


(N, M) = inputs(int)
uf = UnionFind(num_nodes=N)
valid = True
for i in range(M):
    (L, R, D) = inputs(int)
    L -= 1
    R -= 1
    valid = valid and uf.unite(L, R, D)
print('Yes' if valid else 'No')
