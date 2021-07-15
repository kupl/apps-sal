class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        @lru_cache(None)
        def helper(i: int, j: int) -> int:
            if i < 0 or j < 0:
                return 0
            return max([
                helper(i - 1, j - 1) + (A[i] == B[j]),
                helper(i - 1, j),
                helper(i, j - 1)
            ])
        
        return helper(len(A) - 1, len(B) - 1)

