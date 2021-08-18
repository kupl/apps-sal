class DSU:
    def __init__(self, N):
        self.p = list(range(N))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        self.p[xr] = yr


class Solution:
    def primes_set(self, n):
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return self.primes_set(n // i) | set([i])
        return set([n])

    def largestComponentSize2(self, A):
        n = len(A)
        UF = DSU(n)
        primes = defaultdict(list)
        for i, num in enumerate(A):
            pr_set = self.primes_set(num)
            for q in pr_set:
                primes[q].append(i)
        for _, indexes in list(primes.items()):
            for i in range(len(indexes) - 1):
                UF.union(indexes[i], indexes[i + 1])

        return max(Counter([UF.find(i) for i in range(n)]).values())

    def largestComponentSize1(self, A: List[int]) -> int:
        g = set(range(len(A)))
        r = 0
        while g:
            gc = A[g.pop()]
            ri = 1
            while True:
                gm = set()
                gc2 = 1
                for i in g:
                    if gcd(A[i], gc) > 1:
                        ri += 1
                        gm.add(i)
                        gc2 *= A[i]
                if not gm:
                    break
                g -= gm
                gc = gc2
            r = max(r, ri)

        return r

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def largestComponentSize(self, A: List[int]) -> int:

        self.p = list(range(len(A)))

        def factors(n: int) -> set:
            return set(factor for i in range(2, int(n**0.5) + 1) if n % i == 0
                       for factor in (i, n // i))
        d = {}
        g = set(range(len(A)))
        fx = []
        for i, v in enumerate(A):
            f = factors(v)
            f.add(v)
            fx += [f]
            for fi in f:
                l = d.setdefault(fi, [])
                l += [i]

        for di in list(d.values()):
            for a, b in zip(di[1:], di):
                self.p[self.find(a)] = self.find(b)

        return max(Counter(self.find(i) for i in self.p).values())

        r = 0
        while g:
            gi = [g.pop()]
            g1 = [gi]

            while gi:
                gii = gi.pop()
                for f in fx[gii]:
                    for di in d[f]:
                        if di in g:
                            g.remove(di)
                            g1 += [di]
                            gi += [di]
            r = max(r, len(g1))

        return r
