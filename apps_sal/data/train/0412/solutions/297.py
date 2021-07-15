class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        memo= {}
        def rolls(dice, t):
            if t > f * dice:
                memo[(dice, t)] = 0
                return 0
            if dice == 0:
                return t == 0
            if target < 0:
                return 0
            if (dice, t) in memo:
                return memo[(dice, t)]
            solu = 0
            for num in range(1, f + 1):
                solu += rolls(dice - 1, t - num)
            memo[(dice, t)] = solu
            return solu
        return rolls(d, target) % (10**9 + 7)
                
        

