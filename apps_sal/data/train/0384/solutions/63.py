class Solution:

    def sumSubseqWidths(self, A: List[int]) -> int:
        """
        1 2 3
            x
        """
        ret = 0
        mod = 10 ** 9 + 7
        for (i, n) in enumerate(sorted(A)):
            ret = (ret + n * (1 << i)) % mod
            ret = (ret - n * (1 << len(A) - i - 1)) % mod
        return ret
