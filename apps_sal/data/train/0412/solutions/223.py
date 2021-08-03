class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        mod = 1000000007
        dp = [[0] * (d + 1) for i in range(target + 1)]
        for tar in range(1, target + 1):
            if f >= tar:
                dp[tar][1] = 1
        for dice in range(2, d + 1):
            for tar in range(1, target + 1):
                for possVal in range(1, f + 1):
                    if tar - possVal >= 1:
                        dp[tar][dice] = (dp[tar][dice] + dp[tar - possVal][dice - 1]) % mod
        print(dp)
        return dp[-1][-1]
