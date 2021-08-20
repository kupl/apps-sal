class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        memo = {}
        for (j, y) in enumerate(A):
            for (i, x) in enumerate(A[:j]):
                d = y - x
                memo[d, j] = memo.get((d, i), 1) + 1
        return max(memo.values())
