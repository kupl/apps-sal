from collections import Counter


class Solution:

    def distinctSubseqII(self, S: str) -> int:
        res = 1
        endCount = Counter()
        for s in S:
            (res, endCount[s]) = (2 * res - endCount[s], res)
        return (res - 1) % (10 ** 9 + 7)
