class UF:
    def __init__(self):
        self.p = {}
        self.m = {}

    def find_make_set(self, x):
        if not x in self.p:
            self.p[x] = None
            self.m[x] = 1
            return x

        if self.p[x] is None:
            return x
        return self.find_make_set(self.p[x])

    def union(self, a, b):
        repa = self.find_make_set(a)
        repb = self.find_make_set(b)
        if repa != repb:
            self.p[repb] = repa
            self.m[repa] += self.m[repb]
        return repa


class Solution:
    def findLatestStep(self, arr: List[int], m: int) -> int:

        n = len(arr)
        ones = {}
        ans = -1
        uf = UF()

        import collections
        cnt = collections.defaultdict(int)
        for i, a in enumerate(arr):
            ones[a] = 1
            uf.find_make_set(a)
            cnt[1] += 1

            if a - 1 >= 1 and a - 1 in ones:
                rep = uf.find_make_set(a - 1)
                cnt[uf.m[rep]] -= 1

                cnt[1] -= 1

                rep = uf.union(a - 1, a)
                cnt[uf.m[rep]] += 1

            if a + 1 <= n and a + 1 in ones:
                rep = uf.find_make_set(a + 1)
                cnt[uf.m[rep]] -= 1

                rep = uf.find_make_set(a)
                cnt[uf.m[rep]] -= 1

                rep = uf.union(a + 1, a)
                cnt[uf.m[rep]] += 1

            if cnt[m] > 0:
                ans = i + 1

        return ans
