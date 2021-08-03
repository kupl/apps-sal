class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = [1] * len(arr)
        ans = 1
        seen = {}
        for i in range(len(arr)):
            if(arr[i] - difference in seen):
                dp[i] = 1 + dp[seen[arr[i] - difference]]
            seen[arr[i]] = i
        return max(dp)
