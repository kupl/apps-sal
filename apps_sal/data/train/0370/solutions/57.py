class DisjSet:

    def __init__(self, n):
        self.disj_set = [-1] * n

    def find(self, x):
        while self.disj_set[x] >= 0:
            x = self.disj_set[x]
        return x

    def union(self, x, y):
        i = self.find(x)
        j = self.find(y)
        if i == j:
            return
        if self.disj_set[i] < self.disj_set[j]:
            self.disj_set[i] += self.disj_set[j]
            self.disj_set[j] = i
        else:
            self.disj_set[j] += self.disj_set[i]
            self.disj_set[i] = j

    def maxset(self):
        return -min(self.disj_set)


class Solution:

    def largestComponentSize(self, A: List[int]) -> int:

        def factor(n):
            f = []
            while True:
                for i in range(2, int(math.sqrt(n)) + 1):
                    if n % i == 0:
                        f.append(i)
                        n //= i
                        break
                else:
                    f.append(n)
                    break
            return f
        n = len(A)
        disj = DisjSet(n)
        g = {}
        for (i, a) in enumerate(A):
            for f in factor(a):
                if f not in g:
                    g[f] = i
                else:
                    disj.union(i, g[f])
        return disj.maxset()
