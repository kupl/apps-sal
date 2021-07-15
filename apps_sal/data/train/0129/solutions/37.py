class Solution:
    def maxScoreSightseeingPair(self, A: List[int]) -> int:
        
        n = len(A)
        # dp = [0] * n
        # dp[0] = A[0]
        dp = 0
        ans = 0
        for j in range(0,n):
            # ans = A[j]-j + max_i{0, j-1}(A[i]+i)
            #     = A[j]-j] + dp[j-1]
            # dp[j] = max(dp[j-1], A[j]+j)
            # ans = max(ans, A[j]-j + dp[j-1])
            # dp[j] = max(dp[j-1], A[j]+j)
            ans = max(ans, A[j]-j + dp)
            dp = max(dp, A[j]+j)
        # print(dp)
        return ans
