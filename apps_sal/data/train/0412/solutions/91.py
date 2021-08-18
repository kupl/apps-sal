class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [[0 for _ in range(target + 1)]]
        for i in range(1, min(f + 1, target + 1)):
            dp[0][i] = 1
        for i in range(2, d + 1):
            dp.append([0 for _ in range(target + 1)])
            for t in range(i, target + 1):
                for d in range(1, min(t, f + 1, target + 1)):
                    if t - d >= 0 and dp[-2][t - d]:
                        dp[-1][t] += dp[-2][t - d]
            dp.pop(0)
        return (dp[0][-1]) % (10**9 + 7)
