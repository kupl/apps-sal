class Solution:
    def maxSumAfterPartitioning(self, arr: List[int], k: int) -> int:
        
        dp = (len(arr) + 1)  * [0]

        for i in range(0, len(arr)):
            sub_max = 0
            for j in range(k):
                if j <= i:
                    sub_max = max(sub_max, arr[i-j])
                    dp[i + 1] = max(dp[i+1], sub_max * (j + 1) + dp[i-j])
        
        return dp[len(arr)]
