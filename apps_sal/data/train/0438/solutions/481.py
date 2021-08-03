class Solution:
    def find(self, n):
        if self.par[n] == n:
            return n
        else:
            self.par[n] = self.find(self.par[n])
            return self.par[n]

    def union(self, n1, n2):
        p1 = self.find(n1)
        p2 = self.find(n2)
        if self.rank[p1] < self.rank[p2]:
            self.par[p1] = p2
            self.rank[p2] += self.rank[p1]
        elif self.rank[p1] > self.rank[p2]:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.par[p2] = p1
            self.rank[p1] += self.rank[p2]

    def findLatestStep(self, arr: List[int], m: int) -> int:
        N = len(arr)
        self.N = N
        if m == N:
            return N

        self.par = list(range(N + 1))
        self.rank = [0] * (N + 1)
        result = -1
        s = '0' * (N + 1)
        for i, v in enumerate(arr, 1):
            self.rank[v] = 1
            for j in [v - 1, v + 1]:
                if 1 <= j <= N and self.rank[j]:
                    if self.rank[self.find(j)] == m:
                        result = i - 1
                    self.union(j, v)

        for i in range(1, N + 1):
            if self.rank[self.find(i)] == m:
                return N

        return result
