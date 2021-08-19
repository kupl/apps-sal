class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        if not A:
            return 0

        def findPrimes(n):
            for i in range(2, int(n ** 0.5) + 1):
                if n % i == 0:
                    return set([i]) | findPrimes(n // i)
            return set([n])
        findset = list(range(len(A)))

        def find(i):
            while findset[i] != i:
                i = findset[i]
            return i

        def union(i, j):
            (ri, rj) = (find(i), find(j))
            findset[rj] = ri
        primdic = defaultdict(list)
        for (i, num) in enumerate(A):
            ps = findPrimes(num)
            for p in list(ps):
                primdic[p] += (i,)
        for idxs in list(primdic.values()):
            for i in range(len(idxs) - 1):
                union(idxs[i], idxs[i + 1])
        return max(Counter((find(i) for i in range(len(A)))).values())
