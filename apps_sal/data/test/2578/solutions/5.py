class UnionFind:

    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n
        self.num_sets = n

    def find(self, a):
        to_update = []
        while a != self.parent[a]:
            to_update.append(a)
            a = self.parent[a]
        for b in to_update:
            self.parent[b] = a
        return self.parent[a]

    def merge(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return
        if self.size[a] < self.size[b]:
            (a, b) = (b, a)
        self.num_sets -= 1
        self.parent[b] = a
        self.size[a] += self.size[b]

    def set_size(self, a):
        return self.size[self.find(a)]


def main():
    from sys import stdin, stdout

    def read():
        return stdin.readline().rstrip('\n')

    def read_array(sep=None, maxsplit=-1):
        return read().split(sep, maxsplit)

    def read_int():
        return int(read())

    def read_int_array(sep=None, maxsplit=-1):
        return [int(a) for a in read_array(sep, maxsplit)]

    def write(*args, **kwargs):
        sep = kwargs.get('sep', ' ')
        end = kwargs.get('end', '\n')
        stdout.write(sep.join((str(a) for a in args)) + end)

    def write_array(array, **kwargs):
        sep = kwargs.get('sep', ' ')
        end = kwargs.get('end', '\n')
        stdout.write(sep.join((str(a) for a in array)) + end)
    (n, m) = read_int_array()
    uf = UnionFind(n)
    for _ in range(m):
        nums = read_int_array()
        sz = nums[0]
        leader = None
        for i in range(sz):
            p = nums[1 + i] - 1
            if leader is None:
                leader = p
            else:
                uf.merge(p, leader)
    ans = [uf.set_size(i) for i in range(n)]
    write(*ans)


main()
