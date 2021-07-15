class Solution:
    def largestComponentSize(self, A: List[int]) -> int:
        def factor(n):
            res = []
            t = int(math.sqrt(n)) + 1
            for i in range(2, t + 1):
                if n % i == 0:
                    res += [i]
                    while n % i == 0:
                        n //= i
            if n != 1:
                res += [n]
            return res
        uf = [i for i in range(len(A))]
        def root(p):
            while p != uf[p]:
                uf[p] = uf[uf[p]]
                p = uf[p]
            return p
        def union(p, q):
            proot = root(p)
            qroot = root(q)
            uf[proot] = uf[qroot] = proot
        components = collections.defaultdict(list)
        for i, n in enumerate(A):
            for p in factor(n):
                if len(components[p]) > 0:
                    union(components[p][-1], i)
                components[p] += [i]
        cnt = collections.Counter([root(i) for i in uf])
        return cnt.most_common()[0][1]
