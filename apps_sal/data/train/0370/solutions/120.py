class UnionFind:

    def __init__(self, n):
        self.reps = [i for i in range(n)]
        self.size = [1] * n

    def find(self, x):
        while self.reps[x] != x:
            self.reps[x] = self.reps[self.reps[x]]
            x = self.reps[x]
        return x

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        self.reps[x_root] = y_root
        self.size[y_root] += self.size[x_root]
        self.size[x_root] = 0


class Solution:

    def largestComponentSize(self, A: List[int]) -> int:

        def get_prime_factor(n):
            factors = set()
            while n % 2 == 0:
                n //= 2
                factors.add(2)
            while n % 3 == 0:
                n //= 3
                factors.add(3)
            for i in range(5, int(sqrt(n)) + 1):
                while n % i == 0:
                    factors.add(i)
                    n //= i
            if n > 1:
                factors.add(n)
            return factors
        factor2idx = collections.defaultdict(list)
        for i in range(len(A)):
            for factor in get_prime_factor(A[i]):
                factor2idx[factor].append(i)
        uf = UnionFind(len(A))
        for (factor, indices) in list(factor2idx.items()):
            for idx in indices[1:]:
                uf.union(indices[0], idx)
        return max(uf.size)
