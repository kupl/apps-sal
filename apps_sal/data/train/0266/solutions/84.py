class Solution:
    def numSplits(self, s: str) -> int:
        if not s:
            return 0
        l_unique = set([])
        r_unique = set(s)
        good_splits = 0
        for i, x in enumerate(s):
            l_unique.add(x)
            if x not in s[i + 1:]:
                r_unique.discard(x)
            if len(l_unique) == len(r_unique):
                good_splits += 1
        return good_splits
