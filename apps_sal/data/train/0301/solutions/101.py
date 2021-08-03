class Solution:
    def maxUncrossedLines(self, A: List[int], B: List[int]) -> int:

        l = max(len(A), len(B))

        dp = [[-1 for i in range(l + 1)]for j in range(l + 1)]

        def func(indexA, indexB):
            if indexA >= len(A) or indexB >= len(B):
                return 0
            print
            if dp[indexA][indexB] != -1:
                return dp[indexA][indexB]

            if A[indexA] == B[indexB]:
                dp[indexA][indexB] = func(indexA + 1, indexB + 1) + 1
            else:
                dp[indexA][indexB] = max(func(indexA + 1, indexB), func(indexA, indexB + 1))

            return dp[indexA][indexB]

        return func(0, 0)
