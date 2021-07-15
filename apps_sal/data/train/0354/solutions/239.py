from functools import lru_cache
class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        
        @lru_cache(None)
        def roll(val,cons,roll_left):
            if roll_left == 0:
                return 1
            total_ways = 0
            for i in range(6):
                if i == val:
                    continue
                total_ways += roll(i,1,roll_left-1)
            if cons < rollMax[val]:
                total_ways += roll(val,cons+1,roll_left-1)
            return total_ways
        
        return roll(0,0,n) % (10**9 + 7)

