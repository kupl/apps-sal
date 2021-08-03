class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        memo = {}

        def dp(dice, target):
            if((dice, target) in memo):
                return memo[(dice, target)]
            if(dice <= 0 or target <= 0):
                return 0
            if(dice == 1):
                if(target >= 1 and target <= f):
                    return 1
                else:
                    return 0
            rolls = 0
            for i in range(1, f + 1):
                rolls += dp(dice - 1, target - i) % 1000000007
            memo[(dice, target)] = rolls % 1000000007
            return memo[(dice, target)] % 1000000007
        return dp(d, target) % 1000000007
