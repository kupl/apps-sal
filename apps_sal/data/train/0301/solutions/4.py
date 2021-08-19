class Solution:

    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:
        dp = {}

        def func(indexA, indexB):
            if indexA == len(A) or indexB == len(B):
                return 0
            if (indexA, indexB) in dp:
                return dp[indexA, indexB]
            if A[indexA] == B[indexB]:
                dp[indexA, indexB] = func(indexA + 1, indexB + 1) + 1
            else:
                dp[indexA, indexB] = max(func(indexA + 1, indexB), func(indexA, indexB + 1))
            return dp[indexA, indexB]
        return func(0, 0)
