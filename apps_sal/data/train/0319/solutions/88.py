from functools import lru_cache


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        @lru_cache(maxsize=None)
        def score(i):
            if i >= len(stoneValue):
                return 0
            return max([sum(stoneValue[i:i + k]) - score(i + k) for k in [1, 2, 3]])

        s = score(0)
        if s > 0:
            return 'Alice'
        elif s < 0:
            return 'Bob'
        else:
            return 'Tie'
