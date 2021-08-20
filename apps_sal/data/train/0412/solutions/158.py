class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [[0 for _ in range(d)] for _ in range(target + 1)]
        for i in range(1, target + 1):
            dp[i][0] = 1 if i <= f else 0
        for di in range(1, d):
            for t in range(1, target + 1):
                sub_targets = [t - face if t >= face else 0 for face in range(1, f + 1)]
                dp[t][di] = sum([dp[sub][di - 1] for sub in sub_targets])
        return dp[-1][-1] % (10 ** 9 + 7)
