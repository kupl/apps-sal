class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:
        class UF:
            def __init__(self):
                self.size = 1
                self.parent = self

            def find(self):
                if self.parent is not self:
                    self.parent = self.parent.find()
                return self.parent

            def union(self, other):
                p1, p2 = self.find(), other.find()
                if p1 is p2:
                    return

                if p2.size < p1.size:
                    p1, p2 = p2, p1

                p2.size += p1.size
                p1.parent = p2

        groups = {}
        sizes = collections.Counter()

        res = -1
        for i, n in enumerate(arr):
            n -= 1
            groups[n] = g = UF()
            sizes[1] += 1

            if n - 1 in groups:
                sizes[groups[n - 1].find().size] -= 1
                sizes[g.find().size] -= 1
                groups[n - 1].union(g)
                sizes[g.find().size] += 1

            if n + 1 in groups:
                sizes[groups[n + 1].find().size] -= 1
                sizes[g.find().size] -= 1
                groups[n + 1].union(g)
                sizes[g.find().size] += 1

            if sizes[m] > 0:
                res = i + 1

        return res
