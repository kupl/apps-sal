from functools import lru_cache


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        c = 0
        sums = []
        for i in range(len(stoneValue) - 1, -1, -1):
            c += stoneValue[i]
            sums.append(c)

        @lru_cache(None)
        def optimalValue(s):
            if not s:
                return 0
            return max([sums[s - 1] - optimalValue(s - i) for i in range(1, 4) if s - i >= 0])
        half = 0.5 * sum(stoneValue)
        res = optimalValue(len(stoneValue))
        return 'Alice' if res > half else 'Bob' if res < half else 'Tie'
