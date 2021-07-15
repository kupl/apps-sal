class Solution:
    def numRollsToTarget(self, d: int, f: int, target: int) -> int:
    
        memo = {}
        
        def helper(dices, total):
            # print(dices, total)
            if total < 0:
                return 0
            if dices == 0 and total == 0:
                return 1
            if dices > 0 and total == 0:
                return 0
            if dices * f < total:
                memo[(dices, total)] = 0
                return 0

            if (dices, total) in memo:
                return memo[(dices, total)]
            
            ways = 0
            for num in range(1, f + 1):
                ways += helper(dices - 1, total - num)
            
            memo[(dices, total)] = ways
            # print(ways)
            return ways
        
        return helper(d, target) % (10 ** 9 + 7)
