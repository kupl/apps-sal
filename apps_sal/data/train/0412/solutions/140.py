class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp1 = [0 for _ in range(target + 1)]
        dp2 = [0 for _ in range(target + 1)]
        dp1[0] = 1
        mod = 10 ** 9 + 7
        for i in range(1, d + 1):
            for j in range(target + 1):
                for k in range(1, min(j, f) + 1):
                    dp2[j] = (dp2[j] + dp1[j - k]) % mod
            dp1 = dp2
            dp2 = [0 for _ in range(target + 1)]
        return dp1[target] % mod
