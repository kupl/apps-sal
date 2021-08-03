class Solution:
    def distinctSubseqII(self, S: str) -> int:
        res, endwith = 0, collections.Counter()
        for c in S:
            res, endwith[c] = res * 2 + 1 - endwith[c], res + 1

        return res % (7 + 10**9)
