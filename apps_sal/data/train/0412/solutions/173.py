class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, d + 1):
            temp = [0]
            for j in range(1, target + 1):
                x = sum((dp[j - k] if k <= min(j, f) else 0 for k in range(1, f + 1)))
                temp.append(x)
            dp = temp
        return dp[target] % (10 ** 9 + 7)
