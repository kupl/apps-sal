class UF:

    def __init__(self, n):
        self.parent = list(range(n))
        self.size = [1] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        (px, py) = (self.find(x), self.find(y))
        if px != py:
            if self.size[px] < self.size[py]:
                (px, py) = (py, px)
            self.parent[py] = px
            self.size[px] += self.size[py]


class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        prime = [0, 0] + [1] * (int(max(A) ** 0.5 + 1) - 2)
        for i in range(2, int(len(prime) ** 0.5) + 1):
            if prime[i]:
                prime[i * i::i] = [0] * ((len(prime) - 1) // i - i + 1)
        prime = [i for (i, x) in enumerate(prime) if x]
        factor = collections.defaultdict(list)
        for (i, x) in enumerate(A):
            for p in prime:
                if p * p > x:
                    break
                if x % p == 0:
                    factor[p].append(i)
                    while x % p == 0:
                        x //= p
            if x > 1:
                factor[x].append(i)
        uf = UF(len(A))
        for numbers in factor.values():
            for (i, j) in zip(numbers, numbers[1:]):
                uf.union(i, j)
        return max(uf.size)
