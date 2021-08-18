class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        L = max(A) + 5
        spf = [i for i in range(L)]
        for p in range(2, L):
            if spf[p] != p:
                continue
            for i in range(p * p, L, p):
                spf[i] = min(spf[i], p)

        def primes(n):
            while n > 1:
                yield spf[n]
                n //= spf[n]
        rep = [i for i in range(L)]
        sz = [0] * L

        def find(x):
            if rep[x] != x:
                rep[x] = find(rep[x])
            return rep[x]

        def union(x, y):
            rx = find(x)
            ry = find(y)
            if rx == ry:
                return
            rep[rx] = ry
            sz[ry] += sz[rx]
        for x in A:
            if x < 2:
                continue
            ps = list(primes(x))
            sz[find(ps[0])] += 1
            for i in range(len(ps) - 1):
                union(ps[i], ps[i + 1])
        return max(sz)
