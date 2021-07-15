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
    def largestComponentSize(self, A: List[int]) -> int:
        def primes_set(n):
            for i in range(2, int(math.sqrt(n))+1):
                if n % i == 0:
                    return primes_set(n//i) | set([i])
            return set([n])
        
        n = len(A)
        UF = DSU(n)
        primes = defaultdict(list)
        for i, num in enumerate(A):
            pr_set = primes_set(num)
            for q in pr_set: primes[q].append(i)

        for _, indexes in primes.items():
            for i in range(len(indexes)-1):
                UF.union(indexes[i], indexes[i+1])

        return max(Counter([UF.find(i) for i in range(n)]).values())
