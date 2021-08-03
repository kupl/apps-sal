class Solution:
    def minFlipsMonoIncr(self, S: str) -> int:
        dp = 0
        ones = 0

        for c in S:
            if c == '0':
                # 結尾為 1 的翻法的最小步驟數 = 1 + dp[i-1]
                # 結尾為 0 的翻法的最小步驟數 = 前面 1 的個數
                # 所以 dp[i] = min(1 + dp[i-1], # of 1s)
                dp = min(1 + dp, ones)
            else:
                # 結尾為 1 的翻法的最小步驟數 = dp[i-1]
                # 結尾為 0 的翻法的最小步驟數 = 1 + 前面 1 的個數
                # 所以 dp[i] = min(dp[i-1], 1 + # of 1s)
                dp = min(dp, 1 + ones)
                ones += 1

        return dp
