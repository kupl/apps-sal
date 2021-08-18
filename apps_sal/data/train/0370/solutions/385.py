class Solution:
    def primeDecompose(self, num):
        factor = 2
        prime_factors = []
        while num >= factor * factor:
            if num % factor == 0:
                prime_factors.append(factor)
                num = num // factor
            else:
                factor += 1
        prime_factors.append(num)
        return prime_factors

    def largestComponentSize(self, A: List[int]) -> int:
        factorMap = {}

        def find(a):
            if a not in factorMap or factorMap[a] == a:
                factorMap[a] = a
                return a
            else:
                return find(factorMap[a])

        factorCount = {}
        maxCount = 0
        for n in A:
            primeFactors = self.primeDecompose(n)
            pivot = find(primeFactors[0])
            if pivot not in factorCount:
                factorCount[pivot] = 0
            factorCount[pivot] += 1
            for i in range(1, len(primeFactors)):
                root = find(primeFactors[i])
                factorMap[root] = pivot
                if root in factorCount and root != pivot:
                    factorCount[pivot] += factorCount[root]
            maxCount = max(maxCount, factorCount[pivot])

        return maxCount
