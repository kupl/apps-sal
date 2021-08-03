class UnionFind(object):
    def __init__(self, n):
        self.uf = [i for i in range(n)]
        self.size = [1] * n

    def find(self, node):
        if node != self.uf[node]:
            return self.find(self.uf[node])
        else:
            return node

    def union(self, x, y):
        x_r = self.find(x)
        y_r = self.find(y)
        if x_r == y_r:
            return
        self.uf[y_r] = x_r
        self.size[x_r] += self.size[y_r]
        self.size[y_r] = 0


class Solution:
    def largestComponentSize(self, A: List[int]) -> int:

        def prime(n):
            cur = set()
            while n % 2 == 0:
                cur.add(2)
                n //= 2
            for i in range(3, int(math.sqrt(n)) + 1, 2):
                while n % i == 0:
                    cur.add(i)
                    n //= i
            if n > 2:
                cur.add(n)
            return cur

        index = {A[i]: i for i in range(len(A))}
        uf = UnionFind(len(A))
        res = collections.defaultdict(list)
        for i in A:
            for j in prime(i):
                res[j].append(i)
        for i, e in list(res.items()):
            if e:
                root = e[0]
                for j in e[1:]:
                    uf.union(index[root], index[j])
        return max(uf.size)
