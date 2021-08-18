class Solution:
    def maxUniqueSplit(self, s: str) -> int:

        def backtrack(seen, sidx):
            if sidx == len(s):
                self.res = max(self.res, len(seen))
                return
            if len(seen) + len(s) - sidx <= self.res:
                return
            for eidx in range(sidx, len(s)):
                if s[sidx:eidx + 1] not in seen:
                    backtrack(seen | {s[sidx:eidx + 1]}, eidx + 1)
        self.res = 1
        backtrack(set(), 0)
        return self.res
