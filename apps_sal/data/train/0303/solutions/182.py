class Solution:
    def maxSumAfterPartitioning(self, A, K):
        # https://leetcode.com/problems/partition-array-for-maximum-sum/discuss/290863/JavaC%2B%2BPython-DP
        # Use dp (record[i+1]) to record the maximum sum can be obtained from A[0]-A[i]
        # For each position, we loop back 1 to k elements and find the maximum within each range
        # And replace them all with the maximum and try to find the maximum sum based on record[i-k+1]
        n = len(A)
        record = [0] * (n + 1)
        for i in range(n):
            curMax = 0
            for k in range(1, min(K, i + 1) + 1):
                curMax = max(curMax, A[i - k + 1])
                record[i + 1] = max(record[i + 1], record[i - k + 1] + curMax * k)
        return record[n]

        # N = len(A)
        # dp = [0] * (N + 1)
        # for i in range(N):
        #     curMax = 0
        #     for k in range(1, min(K, i + 1) + 1):
        #         curMax = max(curMax, A[i - k + 1])
        #         dp[i+1] = max(dp[i+1], dp[i+1 - k] + curMax * k)
        # return dp[N]
