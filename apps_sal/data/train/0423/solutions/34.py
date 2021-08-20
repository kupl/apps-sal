class Solution:

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        n = len(arr)
        dp = defaultdict(int)
        for i in arr:
            dp[i] = max(dp[i], dp[i - difference] + 1)
        return max(dp.values())
