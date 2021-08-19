class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        uf = UnionFind(len(A))
        prime_index = {}
        for (i, n) in enumerate(A):
            pfs = get_prime_factors(n)
            for p in pfs:
                if p in prime_index:
                    uf.union(i, prime_index[p])
                prime_index[p] = i
        return max(uf.size)


class UnionFind:

    def __init__(self, N):
        self.uf = [i for i in range(N)]
        self.size = [1] * N

    def find(self, x):
        while x != self.uf[x]:
            x = self.uf[x]
        return x

    def union(self, x, y):
        x_root = self.find(x)
        y_root = self.find(y)
        if x_root == y_root:
            return
        if self.size[x_root] > self.size[y_root]:
            self.uf[y_root] = x_root
            self.size[x_root] += self.size[y_root]
            self.size[y_root] = 0
        else:
            self.uf[x_root] = y_root
            self.size[y_root] += self.size[x_root]
            self.size[x_root] = 0


def get_prime_factors(n):
    prime_factors = set()
    while n % 2 == 0:
        prime_factors.add(2)
        n //= 2
    for d in range(3, int(math.sqrt(n)) + 1, 2):
        while n % d == 0:
            prime_factors.add(d)
            n //= d
    if n > 2:
        prime_factors.add(n)
    return prime_factors
