'''input
4
2 5 5 2
'''
from sys import stdin
import collections


def doc(s):
    if hasattr(s, '__call__'):
        s = s.__doc__

    def f(g):
        g.__doc__ = s
        return g
    return f


class heapdict(collections.MutableMapping):
    __marker = object()

    @staticmethod
    def _parent(i):
        return ((i - 1) >> 1)

    @staticmethod
    def _left(i):
        return ((i << 1) + 1)

    @staticmethod
    def _right(i):
        return ((i + 1) << 1)

    def __init__(self, *args, **kw):
        self.heap = []
        self.d = {}
        self.update(*args, **kw)

    @doc(dict.clear)
    def clear(self):
        self.heap.clear()
        self.d.clear()

    @doc(dict.__setitem__)
    def __setitem__(self, key, value):
        if key in self.d:
            self.pop(key)
        wrapper = [value, key, len(self)]
        self.d[key] = wrapper
        self.heap.append(wrapper)
        self._decrease_key(len(self.heap) - 1)

    def _min_heapify(self, i):
        l = self._left(i)
        r = self._right(i)
        n = len(self.heap)
        if l < n and self.heap[l][0] < self.heap[i][0]:
            low = l
        else:
            low = i
        if r < n and self.heap[r][0] < self.heap[low][0]:
            low = r

        if low != i:
            self._swap(i, low)
            self._min_heapify(low)

    def _decrease_key(self, i):
        while i:
            parent = self._parent(i)
            if self.heap[parent][0] < self.heap[i][0]:
                break
            self._swap(i, parent)
            i = parent

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
        self.heap[i][2] = i
        self.heap[j][2] = j

    @doc(dict.__delitem__)
    def __delitem__(self, key):
        wrapper = self.d[key]
        while wrapper[2]:
            parentpos = self._parent(wrapper[2])
            parent = self.heap[parentpos]
            self._swap(wrapper[2], parent[2])
        self.popitem()

    @doc(dict.__getitem__)
    def __getitem__(self, key):
        return self.d[key][0]

    @doc(dict.__iter__)
    def __iter__(self):
        return iter(self.d)

    def popitem(self):
        """D.popitem() -> (k, v), remove and return the (key, value) pair with lowest\nvalue; but raise KeyError if D is empty."""
        wrapper = self.heap[0]
        if len(self.heap) == 1:
            self.heap.pop()
        else:
            self.heap[0] = self.heap.pop(-1)
            self.heap[0][2] = 0
            self._min_heapify(0)
        del self.d[wrapper[1]]
        return wrapper[1], wrapper[0]

    @doc(dict.__len__)
    def __len__(self):
        return len(self.d)

    def peekitem(self):
        """D.peekitem() -> (k, v), return the (key, value) pair with lowest value;\n but raise KeyError if D is empty."""
        return (self.heap[0][1], self.heap[0][0])


del doc
__all__ = ['heapdict']


def create_necessities(arr, n):
    size_heap = heapdict()
    link = dict()

    arr.append(-1)
    count = 1
    for i in range(n + 1):
        if i == 0:
            leader = arr[i]
            size = 1
        else:
            if arr[i] == arr[i - 1]:
                size += 1
            else:
                size_heap[count] = -(size * (10 ** 14)) - ((n - i))
                link[count] = leader

                count += 1
                leader = arr[i]
                size = 1

    next_node = dict()
    prev_node = dict()
    for i in link:
        if i == 1:
            prev_node[i] = None

            if i + 1 < count:
                next_node[i] = i + 1
            else:
                next_node[i] = None
        elif i == count:
            break

        else:
            prev_node[i] = i - 1
            if i + 1 < count:
                next_node[i] = i + 1
            else:
                next_node[i] = None

    return link, size_heap, prev_node, next_node


n = int(stdin.readline().strip())
arr = list(map(int, stdin.readline().split()))

link, size_heap, prev_node, next_node = create_necessities(arr, len(arr))

op = 0
while len(size_heap) > 0:
    node, size = size_heap.popitem()

    if prev_node[node] != None and next_node[node] != None and link[prev_node[node]] == link[next_node[node]]:
        if prev_node[node] in size_heap and next_node[node] in size_heap:

            temp1 = size_heap[prev_node[node]]
            t1 = (-temp1) % (10 ** 14)
            temp2 = size_heap[next_node[node]]
            t2 = (-temp2) % (10 ** 14)
            size_heap[prev_node[node]] = -float('inf')
            size_heap.popitem()
            size_heap[next_node[node]] = -float('inf')
            size_heap.popitem()
            size_heap[prev_node[node]] = temp1 + temp2 + t2

            next_node[prev_node[node]] = next_node[next_node[node]]
            if next_node[next_node[node]] != None:
                prev_node[next_node[next_node[node]]] = prev_node[node]

        else:
            prev_node[next_node[node]] = prev_node[node]
            next_node[prev_node[node]] = next_node[node]
    else:
        prev_node[next_node[node]] = prev_node[node]
        next_node[prev_node[node]] = next_node[node]

    op += 1

print(op)
