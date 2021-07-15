class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
        memo = {}
        def helper(dice, tar):
            if dice == 0:
                return 1 if tar == 0 else 0
            
            if (dice, tar) in memo:
                return memo[(dice, tar)]
            
            res = 0
            for k in range(max(0, tar-f), tar):
                res += helper(dice-1, k)
            
            memo[(dice, tar)] = res
            return res
        
        
        return  helper(d, target) % (10**9 + 7)
