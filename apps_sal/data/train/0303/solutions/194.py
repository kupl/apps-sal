class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0 for i in range(len(arr)+1)]
        
        for i in range(len(arr)):
            val = arr[i]
            for j in range(1, k+1):
                if i + j -1 >= len(arr):
                    break
                val = max(arr[i+j-1], val)
                dp[i+j] = max(dp[i] + val *j, dp[i+j])
        return dp[-1]
