class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        dp = {}
        for i in range( n):
            if arr[i] - difference in dp:
                dp[arr[i]] = dp[arr[i] - difference] + 1
            else:
                dp[arr[i]] = 1
        
        return max(dp.values()) 

