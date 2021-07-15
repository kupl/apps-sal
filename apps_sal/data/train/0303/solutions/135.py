class Solution:
    def maxSumAfterPartitioning(self, A: List[int], K: int) -> int:
        # use dp to solve this question
        n = len(A)
        dp = [0] * (n + 1)
        # dp[i] is the answer for array A[0] ... A[i-1]
        # for j = 1 .. k, 
        #     dp[i] is the max of dp[i-j] + max(A[i-1] ... A[i-j]) * j
        
        # j = 1
        #         dp[i-1] + max(A[i-1]) * 1
        #         dp[i-2] + max(A[i-1], A[i-2]) * 2
        #         dp[i-3] + max(A[i-1], A[i-2], A[i-3]) * 3
        # ...
        #         dp[i-k] + max(A[i-1], ..., A[i-k]) * 3
        
        for i in range(1, n+1):
            for j in range(1, K+1):
                if i-j>=0:
                    dp[i] = max(dp[i], dp[i-j] + max(A[i-j:i]) * j) # from i-j to i-1, with i-1-i+j+1 = j elements
        return dp[-1]
