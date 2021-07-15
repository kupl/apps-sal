class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        memo = {}
        def dp(d,target):
            if d == 0:
                return 1 if target == 0 else 0
            if (d,target) in memo:
                return memo[(d,target)]
            result = 0
            for k in range(max(0,target-f), target):
                result += dp(d-1,k)
            memo[(d,target)] = result
            return memo[(d,target)]
        return dp(d, target) % (10**9 + 7)
