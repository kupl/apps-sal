class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        words = len(A[0])
        dp = [1] * words

        for i in range(words - 2, -1, -1):
            for j in range(i + 1, words):
                if all(row[i] <= row[j] for row in A):
                    dp[i] = max(dp[i], 1 + dp[j])

        return words - max(dp)
