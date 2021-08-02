import numpy as np


def inputs(func=lambda x: x, sep=None, maxsplit=-1):
    return list(map(func, input().split(sep=sep, maxsplit=maxsplit)))


def input_row(n: int, type=np.int, *args, **kwargs):
    return np.fromiter(inputs(type, *args, **kwargs), dtype=type)


def input_2d(nrows: int, ncols: int, type=np.int, *args, **kwargs):
    data = np.zeros((nrows, ncols), dtype=type)
    for i in range(nrows):
        data[i, :] = input_row(ncols, type, *args, **kwargs)
    return data


class Repeat (object):
    __slots__ = [
        'element',
        'times'
    ]

    def __init__(self, element, times: int):
        self.element = element
        self.times = int(times)

    def __len__(self):
        return self.times

    def __iter__(self):
        return iter(self.element for _ in range(self.times))


def repeat(element, times: int):
    return Repeat(element, times)


class IntAddition (object):
    '''整数の加法'''

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


class UnionFind (object):
    '''重み付きUnion-Find木'''

    def __init__(
            self,
            num_nodes=0,
            abelian_operator=IntAddition()):
        self.parent = []
        self.potential = []
        self.op = abelian_operator

        self.extend(num_nodes)

    def append(self):
        self.parent.append(-1)
        self.potential.append(self.op.identity)

    def extend(self, num_nodes):
        self.parent.extend(repeat(-1, num_nodes))
        self.potential.extend(repeat(self.op.identity, num_nodes))

    def root(self, x):
        parent = self.parent[x]
        if 0 <= parent:
            self.parent[x] = self.root(parent)
            self.potential[x] = self.op.operate(
                self.potential[x], self.potential[parent]
            )
            x = self.parent[x]
        return x

    def difference_from_root_to(self, x):
        self.root(x)
        return self.potential[x]

    def size(self, x):
        return -self.parent[self.root(x)]

    def difference(self, x, y):
        if not self.issame(x, y):
            raise RuntimeError('x と y は同じ集合に属していません。')
        return self.op.cancel(
            self.difference_from_root_to(y),
            self.difference_from_root_to(x)
        )

    def unite(self, x, y, difference=None):
        if difference is None:
            difference = self.op.identity

        x, px = self.root(x), self.potential[x]
        y, py = self.root(y), self.potential[y]
        difference = self.op.cancel(difference, py)
        difference = self.op.operate(difference, px)
        if x == y:
            return difference == 0

        if self.size(x) < self.size(y):
            x, y = y, x
            difference = self.op.invert(difference)
        self.parent[x] += self.parent[y]
        self.parent[y] = x
        self.potential[y] = difference

        return True

    def issame(self, x, y):
        return self.root(x) == self.root(y)


N, M = inputs(int)
uf = UnionFind(num_nodes=N)

valid = True
for i in range(M):
    L, R, D = inputs(int)
    L -= 1
    R -= 1

    if not uf.unite(L, R, D):
        valid = False

print(('Yes' if valid else 'No'))
