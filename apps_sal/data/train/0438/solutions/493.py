class UnionFind:

    def __init__(self):
        self.parents = defaultdict(lambda: -1)
        self.ranks = defaultdict(lambda: 1)

    def join(self, a, b):
        (pa, pb) = (self.find(a), self.find(b))
        if pa == pb:
            return
        if self.ranks[pa] > self.ranks[pb]:
            self.parents[pb] = pa
            self.ranks[pa] += self.ranks[pb]
        else:
            self.parents[pa] = pb
            self.ranks[pb] += self.ranks[pa]

    def find(self, a):
        if self.parents[a] == -1:
            return a
        self.parents[a] = self.find(self.parents[a])
        return self.parents[a]


class Solution:

    def findLatestStep(self, arr: List[int], m: int) -> int:
        uf = UnionFind()
        cnt = 0
        ret = -1
        lst = [0] * len(arr)
        for (idx, i) in enumerate(arr):
            i -= 1
            lst[i] = 1
            if i - 1 >= 0 and lst[i - 1]:
                if uf.ranks[uf.find(i - 1)] == m:
                    cnt -= 1
                uf.join(i, i - 1)
            if i + 1 < len(lst) and lst[i + 1]:
                if uf.ranks[uf.find(i + 1)] == m:
                    cnt -= 1
                uf.join(i, i + 1)
            if uf.ranks[uf.find(i)] == m:
                cnt += 1
            if cnt > 0:
                ret = idx + 1
        return ret
