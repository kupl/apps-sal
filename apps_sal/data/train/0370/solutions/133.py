from math import sqrt
import collections


class Solution:

    def primes(self, n):
        for i in range(2, int(math.sqrt(n)) + 1):
            if n % i == 0:
                return self.primes(n // i) | set([i])
        return set([n])

    def find(self, i):
        if self.root[i] == i:
            return i
        self.root[i] = self.find(self.root[i])
        return self.root[i]

    def union(self, i, j):
        ri = self.find(i)
        rj = self.find(j)
        if ri == rj:
            return
        if self.rank[ri] > self.rank[rj]:
            self.root[rj] = ri
        else:
            self.root[ri] = rj
            if self.rank[ri] == self.rank[rj]:
                self.rank[rj] += 1
        return

    def largestComponentSize(self, A: List[int]) -> int:
        self.root = {i: i for i in range(len(A))}
        self.rank = {i: 0 for i in range(len(A))}
        d = collections.defaultdict(set)
        for i in range(len(A)):
            for key in self.primes(A[i]):
                d[key].add(i)
        for key in d:
            temp = list(d[key])
            for x in temp:
                self.union(temp[0], x)
        return max([val for (key, val) in list(collections.Counter([self.find(i) for i in range(len(A))]).items())])
