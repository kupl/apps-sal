class Solution:

    def distinctSubseqII(self, S: str) -> int:
        (res, last) = (1, {})
        for c in S:
            temp = res * 2
            if c in last:
                temp -= last[c]
            last[c] = res
            res = temp
        return (res - 1) % (10 ** 9 + 7)
