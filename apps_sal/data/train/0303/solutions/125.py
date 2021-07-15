
class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        dp = [0] * len(arr)
        
        for i in range(len(arr)):
            print(arr[i])
            max_so_far = arr[i] + (dp[i-1] if i > 0 else 0)
            for j in range(1, min(i+1, k)):
                max_in_range = max(arr[i-j:i+1])
                max_so_far = max(max_so_far, dp[i-j-1] + max_in_range * (j+1))
            dp[i] = max_so_far
        return dp[len(arr)-1]
