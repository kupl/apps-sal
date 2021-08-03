class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[-1 for i in range(len(text2))] for i in range(len(text1))]

        def memoSolve(i, j):
            if i == len(text1) or j == len(text2):
                return 0

            if memo[i][j] >= 0:
                return memo[i][j]

            include = 0
            j2 = text2.find(text1[i], j)
            if j2 != -1:
                include = 1 + memoSolve(i + 1, j2 + 1)
            noTake = memoSolve(i + 1, j)

            memo[i][j] = max(include, noTake)
            return memo[i][j]

        return memoSolve(0, 0)
