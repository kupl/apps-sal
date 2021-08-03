class Solution:
    def largestMultipleOfThree(self, digits: List[int]) -> str:
        dp = [-1, -1, -1]
        for x in sorted(digits, reverse=True):
            r = x % 3
            r1 = 0
            for y in list(dp):
                if y == -1:
                    dp[r] = max(dp[r], x)
                else:
                    dp[(r1 + r) % 3] = max(dp[(r1 + r) % 3], 10 * y + x)
                r1 += 1
        if dp[0] == -1:
            return ''
        else:
            return str(dp[0])
