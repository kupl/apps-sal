from collections import defaultdict
class Solution:
    def dieSimulator(self, n: int, rollMax: List[int]) -> int:
        if n == 1:
            return 6
        cache = {i: defaultdict(int) for i in range(6)}
        cache_new = {i: defaultdict(int) for i in range(6)}
        MOD = 10 ** 9 + 7
        
        # initialize
        for i in range(6):
            cache[i][1] = 1
        
        for i in range(2, n+1):
            for next_dice in range(6):
                # dice occ 1
                for prev_dice in range(6):
                    if prev_dice != next_dice:
                        cache_new[next_dice][1] += sum(cache[prev_dice].values())
                cache_new[next_dice][1] %= MOD
                
                # dice occ more
                for occ in range(2, rollMax[next_dice]+1):
                    cache_new[next_dice][occ] = cache[next_dice][occ-1]
            cache = cache_new
            cache_new = {i: defaultdict(int) for i in range(6)}
            
        res = 0
        for i in range(6):
            res += sum(cache[i].values())
        return res % MOD
