from collections import defaultdict
class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        if not arr:
            return 0
        dp = [1 for _ in range(len(arr))]
        seen = defaultdict(list)
        for i, num in enumerate(arr):
            prev = num - difference
            choices = seen[prev]
            for j in choices:
                dp[i] = max(dp[j] + 1, dp[i])
            seen[num].append(i)        
        return max(dp)
