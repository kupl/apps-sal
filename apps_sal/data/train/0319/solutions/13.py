import math
from functools import lru_cache


class Solution:

    def stoneGameIII(self, stoneValue):
        n = len(stoneValue)

        @lru_cache(None)
        def solve(i):
            nonlocal stoneValue
            nonlocal n
            if i == n:
                return 0
            ans = -math.inf
            cursum = 0
            for j in range(i, i + 3):
                if j < n:
                    cursum += stoneValue[j]
                    ans = max(cursum - solve(j + 1), ans)
            return ans
        ans = solve(0)
        if ans > 0:
            return 'Alice'
        elif ans < 0:
            return 'Bob'
        else:
            return 'Tie'
