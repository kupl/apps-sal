class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp  = [0] * (len(arr) + 1)
        for i in range(1, len(arr) + 1):
            curM = arr[i-1]
            for j in range(1, min(i , k) + 1):
                curM = max(curM, arr[i-j])
                dp[i] = max(dp[i], dp[i-j] + curM * j)
        return dp[-1]
    
    
        # def maxSumAfterPartitioning(self, A, K):
        # N = len(A)
        # dp = [0] * (N + 1)
        # for i in xrange(N):
        #     curMax = 0
        #     for k in xrange(1, min(K, i + 1) + 1):
        #         curMax = max(curMax, A[i - k + 1])
        #         dp[i] = max(dp[i], dp[i - k] + curMax * k)
        # return dp[N - 1]

