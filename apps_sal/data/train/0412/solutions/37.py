class Solution:
    # @lru_cache(maxsize=None)
    # def numRollsToTarget(self, d: int, f: int, target: int) -> int:
#         mod = 1e9 + 7
#         if target < 0 or d < 0:
#             return 0

#         if target == 0 and d == 0:
#             return 1

#         ways = 0
#         for dice in range(1, 1 + f):
#             ways += self.numRollsToTarget(d - 1, f, target - dice
#             )
#         return int(ways % mod)
    
#         dp = [0] * (1 + target)
#         dp[0] = 1
#         mod = 1e9 + 7

#         for rep in range(d):
#             newDP = [0] * (1 + target)
#             for i in range(1, 1 + f):
#                 for j in range(1, 1 + target):
#                     if i <= j:
#                         newDP[j] += dp[j - i]
#                         newDP[j] %= mod
#             dp = newDP
#         return int(dp[-1])

    # @lru_cache(maxsize=None)
    def numRollsToTarget(self, d, f, target, result=0):
#         MOD = 7 + 1e9
#         if d == 0:
#             return target == 0

#         for i in range(1, f + 1):
#             result = (result + self.numRollsToTarget(d - 1, f, target - i)) % MOD

#         return int(result)
        
        MOD = 7 + 1e9
        dp = [0] * (1 + target)
        dp[0] = 1
        for i in range(1, 1 + d):
            newDP = [0] * (1 + target)
            prev = dp[0]
            for j in range(1, 1 + target):
                newDP[j] = prev
                prev = (prev + dp[j]) % MOD
                if j >= f:
                    prev = (prev - dp[j - f] + MOD) % MOD
            dp = newDP
        return int(dp[-1])
