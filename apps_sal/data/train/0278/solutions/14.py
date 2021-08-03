class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        dp = [-1, -1, -1]
        for x in sorted(digits)[::-1]:
            for a in dp[:] + [0]:
                y = a * 10 + x
                dp[y % 3] = max(dp[y % 3], y)
        return str(dp[0]) if dp[0] >= 0 else ''
