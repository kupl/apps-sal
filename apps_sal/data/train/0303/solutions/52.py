class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0 for i in range(len(arr))]
        for i in range(k):
            dp[i] = (i+1)*max(arr[:i+1])
        for i in range(k,len(arr)):
            for j in range(k):
                dp[i] = max(dp[i], dp[i-j-1]+(j+1)*max(arr[i-j:i+1]))
        return dp[len(arr)-1]

