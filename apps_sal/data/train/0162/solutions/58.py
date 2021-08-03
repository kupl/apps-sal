class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = [[-1 for i in range(len(text2))] for i in range(len(text1))]

        def memoSolve(i, j):
            if i == len(text1) or j == len(text2):
                return 0

            if memo[i][j] >= 0:
                return memo[i][j]

            answer = 0
            if text1[i] == text2[j]:
                answer = 1 + memoSolve(i + 1, j + 1)
            else:
                answer = max(memoSolve(i + 1, j), memoSolve(i, j + 1))
            memo[i][j] = answer
            return memo[i][j]

        return memoSolve(0, 0)
