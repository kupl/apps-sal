class Solution:

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        (dp, res) = (collections.defaultdict(int), 0)
        for x in arr:
            dp[x] = max(1, dp[x])
            res = max(res, dp[x])
            dp[x + difference] = max(dp[x + difference], dp[x] + 1)
        return res
