class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [1 if i < f else 0 for i in range(target)]
        for n in range(2, d + 1):
            new_dp = [0 for _ in range(target)]
            cumsum = 0
            for i in range(target - 1):
                cumsum += dp[i]
                if i >= f:
                    cumsum -= dp[i - f]
                new_dp[i + 1] = cumsum
            dp = new_dp
        return dp[-1] % (10 ** 9 + 7)
