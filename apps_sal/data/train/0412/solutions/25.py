class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        memo = {}
        
        def helper(dice, t):
            if dice == 0:
                return 1 if t == 0 else 0
            
            if (dice, t) in memo:
                return memo[(dice, t)]
            
            res = 0
            for k in range(max(0, t-f), t):
                res += helper(dice-1, k)
            
            memo[(dice, t)] = res
            return res
        
        return helper(d, target) %(10**9 + 7)
