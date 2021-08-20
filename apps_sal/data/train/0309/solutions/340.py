class Solution:

    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = list((dict() for i in range(len(A))))
        maxsize = 0
        for i in range(1, len(A)):
            for j in range(0, i):
                if A[j] - A[i] in dp[j]:
                    dp[i][A[j] - A[i]] = dp[j][A[j] - A[i]] + 1
                else:
                    dp[i][A[j] - A[i]] = 1
                maxsize = max(maxsize, dp[i][A[j] - A[i]])
        return maxsize + 1
