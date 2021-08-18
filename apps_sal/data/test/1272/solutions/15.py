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
        '''
        xとyは-=1して使う
        '''
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


def __starting_point():
    N, M = list(map(int, input().split()))
    bridges = [tuple(map(int, input().split())) for _ in range(M)]

    answer_list = []
    total = N * (N - 1) // 2
    answer_list.append(total)
    union_find = UnionFind(N)
    for i in range(M - 1, 0, -1):
        A, B = bridges[i]
        A -= 1
        B -= 1
        if not union_find.same(A, B):
            total -= union_find.size(A) * union_find.size(B)
            union_find.union(A, B)

        answer_list.append(total)

    len_answer = len(answer_list)
    for i in range(len_answer - 1, -1, -1):
        print((answer_list[i]))


__starting_point()
