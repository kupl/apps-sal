class Solution:
    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        dp = collections.defaultdict(int)
        ans = 0
        for element in arr:
            dp[element] = dp[element - difference] + 1
            ans = max(dp[element], ans)

        return ans
