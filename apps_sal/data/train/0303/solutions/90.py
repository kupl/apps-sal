class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        n = len(arr)
        dp = [0]*n
        currMax = 0
        
        for i in range(n):
            if i < k:
                currMax = max(currMax,arr[i])
                dp[i] = currMax * (i+1)
            else:
                currMax = 0
                for j in range(1,k+1):
                    currMax = max(currMax,arr[i-j+1])
                    dp[i] = max(dp[i], dp[i-j]+currMax*j)
        return dp[n-1]
                    

