class Solution:

    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        if d == 1:
            return int(f >= target)
        dp = [[0] * target for _ in range(d)]
        f = min(f, target)
        for i in range(f):
            dp[0][i] = 1
        for i in range(1, d):
            for j in range(i, target):
                for face in range(1, f + 1):
                    if face > j:
                        break
                    dp[i][j] = (dp[i - 1][j - face] + dp[i][j]) % (1000000000.0 + 7)
        return int(dp[-1][-1])
