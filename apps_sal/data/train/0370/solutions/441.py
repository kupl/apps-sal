class Solution:

    def largestComponentSize(self, A: List[int]) -> int:
        self.uf_table = [idx for idx in range(100001)]

        def find(p):
            if self.uf_table[p] != p:
                self.uf_table[p] = find(self.uf_table[p])
            return self.uf_table[p]

        def union(p, q):
            rootp = find(p)
            rootq = find(q)
            if rootp != rootq:
                self.uf_table[rootp] = rootq
        for x in A:
            for factor in range(2, int(sqrt(x)) + 1):
                if x % factor == 0:
                    union(x, factor)
                    union(x, x // factor)
        results = [0 for _ in range(100001)]
        for x in A:
            results[find(x)] += 1
        return max(results)
