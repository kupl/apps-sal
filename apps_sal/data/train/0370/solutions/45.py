class UF:
    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.s = [1] * n

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def unite(self, x, y):  # x and y are roots
        if self.s[x] < self.s[y]:
            x, y = y, x
        self.p[y] = x
        self.s[x] += self.s[y]
        return x


class Solution:
    M = 100000
    sieve = [0] * (M + 1)
    for i in range(2, M + 1):
        if sieve[i] != 0:
            continue
        for j in range(1, M // i + 1):
            sieve[j * i] = i

    def largestComponentSize(self, A: List[int]) -> int:
        n = len(A)
        g = UF(n)
        primes = defaultdict(list)
        for i, num in enumerate(A):
            while num > 1:
                q = self.sieve[num]
                primes[q].append(i)
                while num % q == 0:
                    num //= q

        for l in primes.values():
            root = g.find(l[0])
            for i in l[1:]:
                node = g.find(i)
                if node != root:
                    root = g.unite(root, node)

        return max(g.s)
