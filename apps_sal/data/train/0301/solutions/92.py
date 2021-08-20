class Solution:

    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:

        @lru_cache(maxsize=None)
        def helper(a_idx, b_idx):
            if a_idx == len(A) or b_idx == len(B):
                return 0
            c1 = 0
            if A[a_idx] == B[b_idx]:
                c1 = 1 + helper(a_idx + 1, b_idx + 1)
            c2 = helper(a_idx + 1, b_idx)
            c3 = helper(a_idx, b_idx + 1)
            return max(c1, c2, c3)
        return helper(0, 0)
