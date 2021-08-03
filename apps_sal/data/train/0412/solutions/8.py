class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        dp = [[0] * (target + 1) for i in range(d + 1)]
        MOD = 1000000007
        dp[0][0] = 1
        for dice in range(1, d + 1):
            for target in range(1, target + 1):
                if(target > dice * f):
                    continue
                else:
                    face = 1
                    while(face <= f and face <= target):
                        dp[dice][target] = (dp[dice][target] + dp[dice - 1][target - face]) % MOD
                        face += 1
        return dp[-1][-1]
