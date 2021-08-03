
class Primes:
    def __init__(self):
        M = ceil(sqrt(100000)) + 1
        isPrime = [True] * M
        k = 2
        while k < M:
            n = 2
            while k * n < M:
                isPrime[k * n] = False
                n += 1
            k += 1
            while k < M and not isPrime[k]:
                k += 1

        self.primes = [k for k in range(2, M) if isPrime[k]]


class Solution:
    primes = Primes().primes

    def largestComponentSize(self, A: List[int]) -> int:

        def getPrimeFactors(a):
            ans = []
            for p in Solution.primes:
                if p * p > a:
                    break
                if a % p == 0:
                    ans.append(p)
                    while True:
                        a = a // p
                        if a % p != 0:
                            break
            if a > 1:
                ans.append(a)
            return ans

        N = len(A)
        D = defaultdict(list)
        for k in range(N):
            a = A[k]
            ap = getPrimeFactors(a)
            for p in ap:
                D[p].append(k)
        dsu = DSU(N)
        for p, indexList in list(D.items()):
            n = len(indexList)
            for i in range(n - 1):
                dsu.union(indexList[i], indexList[i + 1])
        return max(dsu.size)


class DSU:  # Disjoint Set Union data structure

    def __init__(self, size):
        self.size = [1] * (size + 1)
        self.parent = [i for i in range(size + 1)]

    def find(self, i):

        # Path halving... replaces only every other parent pointer with grandparent
        # was fastest at 976ms
        while self.parent[i] != i:
            i = self.parent[i] = self.parent[self.parent[i]]
        return i

        # Path splitting way... let to 980ms... replacing every parent with grandparent
        # while self.parent[i] != i:
        ##    i, self.parent[i] = self.parent[i], self.parent[self.parent[i]]
        # return i

        # The simplest recursive way... led to 1012ms
        # if i != self.parent[i]:
        ##    self.parent[i] = self.find(self.parent[i])
        # return self.parent[i]

    def union(self, i, j):
        i = self.find(i)
        j = self.find(j)

        if i == j:
            return i

        if self.size[i] > self.size[j]:
            i, j = j, i

        self.parent[i] = j
        self.size[j] += self.size[i]

        return j
