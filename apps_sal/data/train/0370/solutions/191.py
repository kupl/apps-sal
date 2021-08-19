class Find:

    def __init__(self, A):
        self.l = list(range(len(A)))

    def find(self, e):
        if self.l[e] != e:
            self.l[e] = self.find(self.l[e])
        return self.l[e]

    def union(self, x, y):
        a = self.find(x)
        b = self.find(y)
        self.l[a] = b

    def primes(self, n):
        for i in range(int(math.sqrt(n)) - 1):
            if n % (i + 2) == 0:
                return self.primes(n // (i + 2)) | set([i + 2])
        return set([n])


class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        factors = defaultdict(list)
        find = Find(A)
        for i in range(len(A)):
            c = find.primes(A[i])
            for j in c:
                factors[j].append(i)
        for (x, i) in list(factors.items()):
            for k in range(len(i) - 1):
                find.union(i[k], i[k + 1])
        counts = list(Counter([find.find(i) for i in range(len(A))]).values())
        return max(counts)
