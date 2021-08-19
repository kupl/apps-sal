class Solution:

    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        memo = {}

        def helper(A, B, a, b):
            if (a, b) in memo:
                return memo[a, b]
            ret = 0
            if a == len(A) or len(B) == b:
                return 0
            if A[a] == B[b]:
                memo[a, b] = 1 + helper(A, B, a + 1, b + 1)
                return memo[a, b]
            ret = max(ret, helper(A, B, a, b + 1), helper(A, B, a + 1, b))
            memo[a, b] = ret
            return ret
        return helper(A, B, 0, 0)
