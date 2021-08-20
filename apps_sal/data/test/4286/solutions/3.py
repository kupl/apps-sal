def read_nums():
    return [int(x) for x in input().split()]


class UnionFind:

    def __init__(self, size):
        self._parents = list(range(size))
        self._sizes = [1 for _ in range(size)]

    def _root(self, a):
        while a != self._parents[a]:
            self._parents[a] = self._parents[self._parents[a]]
            a = self._parents[a]
        return a

    def find(self, a, b):
        return self._root(a) == self._root(b)

    def union(self, a, b):
        (a, b) = (self._root(a), self._root(b))
        if self._sizes[a] < self._sizes[b]:
            self._parents[a] = b
            self._sizes[b] += self._sizes[a]
        else:
            self._parents[b] = a
            self._sizes[a] += self._sizes[b]


def count_result(num_vertex, edges):
    uf = UnionFind(num_vertex)
    res = 0
    for (start, end, cost) in edges:
        if uf.find(start, end):
            continue
        else:
            uf.union(start, end)
            res += cost
    return res


def main():
    (n, m) = read_nums()
    vertex_nums = read_nums()
    edges = []
    for i in range(m):
        nums = read_nums()
        nums[0] -= 1
        nums[1] -= 1
        edges.append(tuple(nums))
    min_index = min([x for x in zip(vertex_nums, list(range(n)))], key=lambda x: x[0])[1]
    for i in range(n):
        if i != min_index:
            edges.append((min_index, i, vertex_nums[min_index] + vertex_nums[i]))
    edges = sorted(edges, key=lambda x: x[2])
    print(count_result(n, edges))


def __starting_point():
    main()


__starting_point()
