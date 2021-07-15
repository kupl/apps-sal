class DisjointSet:
    def __init__(self, num):
        self.forest = list(range(num))

    def find(self, x):
        if self.forest[x] != x:
            self.forest[x] = self.find(self.forest[x])
        return self.forest[x]

    def union(self, x, y):
        self.forest[self.find(x)] = self.find(y)


class Solution:
    def largestComponentSize(self, arr):
        n = len(arr)
        ds = DisjointSet(n)
        primesDict = defaultdict(list)
        for i, num in enumerate(arr):
            primes = self.getPrimes(num)
            for p in primes:
                primesDict[p].append(i)

        for li in primesDict.values():
            for i in range(len(li)-1):
                ds.union(li[i], li[i+1])

        return max(Counter([ds.find(i) for i in range(n)]).values())

    def getPrimes(self, num):
        for i in range(2, int(math.sqrt(num)) + 1):
            if num % i == 0:
                return self.getPrimes(num // i) | {i}
        return {num}
