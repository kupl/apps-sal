class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        dp = 0
        ones = 0

        for c in S:
            if c == '0':
                dp = min(1 + dp, ones)
            else:
                dp = min(dp, 1 + ones)
                ones += 1

        return dp
