class Solution:

    def racecar(self, target: int) -> int:
        dp = [0, 1, 4] + [float('inf')] * target
        for i in range(3, target + 1):
            k = i.bit_length()
            if i == 2 ** k - 1:
                dp[i] = k
                continue
            for j in range(k - 1):
                dp[i] = min(dp[i], dp[i - 2 ** (k - 1) + 2 ** j] + k - 1 + j + 2)
            if 2 ** k - 1 - i < i:
                dp[i] = min(dp[i], dp[2 ** k - 1 - i] + k + 1)
        return dp[target]
