class Solution:

    def longestSubsequence(self, arr: List[int], difference: int) -> int:
        if not arr:
            return 0
        dp = dict()
        for num in arr:
            prev = num - difference
            if prev in dp:
                dp[num] = 1 + dp.get(prev, 0)
            else:
                dp[num] = 1
        return max(dp.values())
