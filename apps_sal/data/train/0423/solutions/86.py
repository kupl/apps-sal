from collections import Counter

class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        
        max_len = 0
        dp = Counter()
        for i in range(len(arr)):
            dp[arr[i]] = max((dp[arr[i] - difference]) + 1, dp[arr[i]])
            max_len = max(max_len, dp[arr[i]])
        
        return max_len
