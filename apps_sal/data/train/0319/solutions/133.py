from functools import lru_cache
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        @lru_cache(maxsize=None)
        def score(i):
            if i >= N: return 0
            return max(stoneValue[i] - score(i+1),
                   sum(stoneValue[i:i+2]) - score(i+2),
                   sum(stoneValue[i:i+3]) - score(i+3))
        N = len(stoneValue)
        s = score(0)
        if s > 0: return 'Alice'
        elif s < 0: return 'Bob'
        else: return 'Tie'
