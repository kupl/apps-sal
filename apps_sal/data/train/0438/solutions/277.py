class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        output = -1
        uf = UF()
        seen = set()
        for step, idx in enumerate(arr, 1):
            uf.add(idx)
            seen.add(idx)
            if idx - 1 in seen:
                uf.join(idx - 1, idx)
            if idx + 1 in seen:
                uf.join(idx, idx + 1)
            if uf.size_counts[m]:
                output = step
        return output


class UF:

    def __init__(self):
        self.parents = {}
        self.sizes = {}
        self.size_counts = collections.Counter()

    def add(self, n):
        self.parents[n] = n
        self.sizes[n] = 1
        self.size_counts[1] += 1

    def find(self, n):
        p = self.parents
        while p[n] != n:
            p[n] = p[p[n]]
            n = p[n]
        return n

    def join(self, a, b):
        a = self.find(a)
        b = self.find(b)
        if a == b:
            return

        s = self.sizes
        sc = self.size_counts
        sc[s[a]] -= 1
        sc[s[b]] -= 1
        sc[s[a] + s[b]] += 1

        p = self.parents
        if s[a] < s[b]:
            p[a] = b
            s[b] += s[a]
        else:
            p[b] = a
            s[a] += s[b]
