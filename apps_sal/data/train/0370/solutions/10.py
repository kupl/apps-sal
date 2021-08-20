class UF:

    def __init__(self, n):
        self.p = [i for i in range(n)]
        self.s = [1] * n

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]


class Solution:
    M = 100000
    sieve = [0] * (M + 1)
    for i in range(2, M + 1):
        if sieve[i] != 0:
            continue
        for j in range(1, M // i + 1):
            sieve[j * i] = i

    def largestComponentSize(self, A: List[int]) -> int:
        g = UF(len(A))
        primes = defaultdict(list)
        for (i, num) in enumerate(A):
            tmp = -1
            while num > 1:
                q = self.sieve[num]
                num //= q
                if q != tmp:
                    primes[q].append(i)
                    tmp = q
        for l in primes.values():
            root = g.find(l[0])
            for i in l[1:]:
                node = g.find(i)
                if node != root:
                    if g.s[root] < g.s[node]:
                        (root, node) = (node, root)
                    g.p[node] = root
                    g.s[root] += g.s[node]
        return max(g.s)
