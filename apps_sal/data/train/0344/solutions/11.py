class Solution:
    def minDeletionSize(self, A):
        W = len(A[0])
        dp = [1] * W
        for j in range(1, W):
            for i in range(j):
                if all(row[i] <= row[j] for row in A):
                    dp[j] = max(dp[i]+1, dp[j])
        return W - max(dp)
