from functools import lru_cache
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        # time complexity: O(n)
        # space complexity: O(n)
        @lru_cache(maxsize=None)
        def score(i):
            if i >= len(stoneValue): return 0
            return max([sum(stoneValue[i:i+1]) - score(i+1),
                        sum(stoneValue[i:i+2]) - score(i+2),
                        sum(stoneValue[i:i+3]) - score(i+3)])
            #return max([sum(stoneValue[i:i+k]) - score(i+k) for k in [1,2,3]])
        
        s = score(0)
        if s > 0: return 'Alice'
        elif s < 0: return 'Bob'
        else: return 'Tie'
