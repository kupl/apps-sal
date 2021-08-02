import sys
input = sys.stdin.readline


class UnionFind():
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def find(self, x):
        if self.parents[x] < 0:
            return x
        else:
            self.parents[x] = self.find(self.parents[x])
            return self.parents[x]

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def size(self, x):
        return -self.parents[self.find(x)]

    def same(self, x, y):
        return self.find(x) == self.find(y)

    def members(self, x):
        root = self.find(x)
        return [i for i in range(self.n) if self.find(i) == root]

    def roots(self):
        return [i for i, x in enumerate(self.parents) if x < 0]

    def group_count(self):
        return len(self.roots())

    def all_group_members(self):
        return {r: self.members(r) for r in self.roots()}

    def __str__(self):
        return '\n'.join('{}: {}'.format(r, self.members(r)) for r in self.roots())


def main():
    n, m = map(int, input().split())
    abl = []
    for _ in range(m):
        a, b = map(int, input().split())
        abl.append([a, b])

    uf = UnionFind(n)
    ans_r = []
    curr_ans_minus = 0
    for ab in reversed(abl):
        a, b = ab
        if not uf.same(a - 1, b - 1):
            a_size = uf.size(a - 1)
            b_size = uf.size(b - 1)
            curr_ans_minus += (a_size + b_size) * (a_size + b_size - 1) // 2
            curr_ans_minus -= (a_size * (a_size - 1) // 2 + b_size * (b_size - 1) // 2)
            uf.union(a - 1, b - 1)
        ans_r.append(curr_ans_minus)

    all_sum = n * (n - 1) // 2
    for v in reversed(ans_r[:-1]):
        print(all_sum - v)
    print(all_sum)


def __starting_point():
    main()


__starting_point()
