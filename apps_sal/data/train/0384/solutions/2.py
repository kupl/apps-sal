class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        '''
        1 2 3
            x
        '''
        ret = 0
        for i, n in enumerate(sorted(A)):
            ret += n * pow(2, i)
            ret -= n * pow(2, len(A) - i - 1)
            ret %= 10**9 + 7

        return ret
