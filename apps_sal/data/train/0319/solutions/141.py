from functools import lru_cache
class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        @lru_cache
        def score(i):
            if i == N - 1: return stoneValue[i]
            if i == N - 2: 
                return max(stoneValue[i] + stoneValue[i+1],
                          stoneValue[i] - stoneValue[i+1],)
            if i == N - 3:
                return max(sum(stoneValue[i:]), stoneValue[i] - score(i+1),
                          sum(stoneValue[i:i+2]) - score(i+2))
            return max(stoneValue[i] - score(i+1),
                   sum(stoneValue[i:i+2]) - score(i+2),
                   sum(stoneValue[i:i+3]) - score(i+3))
        N = len(stoneValue)
        s = score(0)
        if s > 0: return 'Alice'
        elif s < 0: return 'Bob'
        else: return 'Tie'
