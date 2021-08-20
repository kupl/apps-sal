class Solution:

    def largestComponentSize(self, A):
        n = len(A)
        primes = collections.defaultdict(list)
        parents = [i for i in range(n)]

        def find(x):
            if parents[x] != x:
                return find(parents[x])
            return parents[x]

        def union(x, y):
            (xr, yr) = (find(x), find(y))
            if xr > yr:
                parents[xr] = yr
            else:
                parents[yr] = xr

        def primeSet(N):
            for i in range(2, int(math.sqrt(N)) + 1):
                if N % i == 0:
                    return {i} | primeSet(N // i)
            return {N}
        for (i, num) in enumerate(A):
            for q in primeSet(num):
                primes[q] += [i]
        for group in primes.values():
            for i in range(len(group) - 1):
                union(group[i], group[i + 1])
        return max(Counter([find(i) for i in range(n)]).values())
