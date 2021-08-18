class Solution:
    def longestArithSeqLength(self, A: List[int]) -> int:
        dp = [{} for _ in range(len(A))]
        for i in range(len(A) - 1):
            for j in range(i + 1, len(A)):
                diff = A[j] - A[i]
                diffMap = dp[i]
                dp[j][diff] = diffMap.get(diff, 1) + 1

        maxLength = 0

        for i in range(len(A)):
            for diff in dp[i]:
                if dp[i][diff] > maxLength:
                    maxLength = dp[i][diff]

        return maxLength
