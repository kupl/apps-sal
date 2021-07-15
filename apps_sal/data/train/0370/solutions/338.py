class DisjointSet:
    def __init__(self, n):
        self.set = list(range(n))
    def find(self, i):
        if self.set[i] != i:
            self.set[i] = self.find(self.set[i])
        return self.set[i]
        
    def union(self, i, j):
        ii, jj = self.find(i), self.find(j)
        self.set[ii] = jj

class Solution:
    def primeFactors(self,n):
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return self.primeFactors(n//i) | set([i])
        return set([n])
        
    def largestComponentSize(self, A):
        n = len(A)
        unionFind = DisjointSet(n)
        primes = defaultdict(list)
        for i, num in enumerate(A):
            pr_set = self.primeFactors(num)
            for q in pr_set: primes[q].append(i)
        for _, indexes in list(primes.items()):
            for i in range(len(indexes)-1):
                unionFind.union(indexes[i], indexes[i+1])
        return max(Counter([unionFind.find(i) for i in range(n)]).values())

