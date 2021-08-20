class Solution:

    def racecar(self, target: int) -> int:
        dp = [0, 1, 4] + [float('inf')] * (target - 2)
        for i in range(3, target + 1):
            k = math.log2(i + 1)
            if int(k) == k:
                dp[i] = int(k)
                continue
            k = int(k)
            for m in range(0, k):
                dp[i] = min(dp[i], dp[i - 2 ** k + 2 ** m] + k + m + 2)
            if i > 2 ** (k + 1) - 1 - i:
                dp[i] = min(dp[i], dp[2 ** (k + 1) - 1 - i] + k + 1 + 1)
        return dp[target]
