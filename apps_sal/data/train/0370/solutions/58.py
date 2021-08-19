class Solution:

    def largestComponentSize(self, A: List[int]) -> int:

        def pfactorization(a):
            N = a
            if a >= 2 and a % 2 == 0:
                Gp[2].append(N)
                Gn[N].append(2)
                while a % 2 == 0:
                    a //= 2
            for d in range(3, math.floor(a ** (1 / 2)) + 1, 2):
                if d > a:
                    break
                if a % d == 0:
                    Gn[N].append(d)
                    Gp[d].append(N)
                    while a % d == 0:
                        a //= d
            if a > 1:
                Gp[a].append(N)
                Gn[N].append(a)

        def dfs(curr):
            if curr in seenNodes:
                return 0
            seenNodes.add(curr)
            total = 1
            for p in Gn[curr]:
                if p in seenPrimes:
                    continue
                seenPrimes.add(p)
                for owner in Gp[p]:
                    total += dfs(owner)
            return total
        Gp = collections.defaultdict(list)
        Gn = collections.defaultdict(list)
        for a in A:
            pfactorization(a)
        (seenPrimes, seenNodes) = (set(), set())
        return max([dfs(a) for a in A])
