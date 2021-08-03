class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        dp = [-1] + [len(s)] * 31
        mask = 0
        res = 0
        for i, c in enumerate(s):
            if c in 'aeiou':
                mask ^= 1 << 'aeiou'.index(c)

            dp[mask] = min(dp[mask], i)
            res = max(res, i - dp[mask])

        return res
