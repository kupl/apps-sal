class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [0] * (target + 1)
        dp[0] = 1
        for i in range(1, d + 1):
            temp = [0] * (target + 1)
            # iterate each tot from 1 to target
            for j in range(1, target + 1):
                # k is each face
                temp[j] = sum(dp[j - k] if k <= j else 0 for k in range(1, f + 1))
            dp = temp
        return dp[target] % (10**9 + 7)
