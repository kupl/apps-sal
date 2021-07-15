class Solution:
    def sumSubseqWidths(self, A: List[int]) -> int:
        A.sort()
        ret = 0
        for i in range(len(A)):
            # how many subseq contain me as the min/max?
            ret -= A[i]<<(len(A)-i-1)
            ret += A[i]<<i
        return ret%(10**9+7)
