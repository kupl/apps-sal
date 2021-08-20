class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        parents = {val: val for val in A}
        sizes = {val: 1 for val in A}
        factorprez = {}
        maxsize = 0

        def union(one, two):
            r1 = findroot(one)
            r2 = findroot(two)
            if r1 == r2:
                return sizes[r1]
            (big, small) = (r1, r2) if sizes[r1] > sizes[r2] else (r2, r1)
            parents[small] = big
            sizes[big] += sizes[small]
            return sizes[big]

        def findroot(node):
            if parents[node] != node:
                node = findroot(parents[node])
            return parents[node]

        def primes_before(val):
            candidates = [True] * (val + 1)
            primes = []
            for i in range(2, len(candidates)):
                if not candidates[i]:
                    continue
                primes.append(i)
                for j in range(i, val + 1, i):
                    candidates[j] = False
            return primes
        primes = primes_before(100000)
        primeset = set(primes)
        for val in A:
            sval = val
            prime_idx = 0
            while sval not in primeset and primes[prime_idx] <= sval:
                if sval % primes[prime_idx] == 0:
                    if primes[prime_idx] in factorprez:
                        maxsize = max(maxsize, union(val, factorprez[primes[prime_idx]]))
                    else:
                        factorprez[primes[prime_idx]] = val
                    while sval % primes[prime_idx] == 0:
                        sval //= primes[prime_idx]
                prime_idx += 1
            if sval in primeset:
                if sval in factorprez:
                    maxsize = max(maxsize, union(val, factorprez[sval]))
                else:
                    factorprez[sval] = val
        return maxsize
