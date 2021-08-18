from functools import lru_cache


class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        @lru_cache(None)
        def getScore(idx, aliceNext):
            if idx == n:
                return 0
            if aliceNext:
                res = -float('inf')
                t = 0
                for i in range(3):
                    if idx + i == n:
                        break
                    t += values[idx + i]
                    res = max(res, t + getScore(idx + i + 1, False))
                return res
            else:
                res = float('inf')
                t = 0
                for i in range(3):
                    if idx + i == n:
                        break
                    t += values[idx + i]
                    res = min(res, -t + getScore(idx + i + 1, True))
                return res
        values = stoneValue
        n = len(values)
        ans = getScore(0, True)

        ans2 = 'Tie'
        if ans > 0:
            ans2 = 'Alice'
        if ans < 0:
            ans2 = 'Bob'
        return ans2
