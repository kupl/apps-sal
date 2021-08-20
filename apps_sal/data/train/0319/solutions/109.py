class Solution:

    def stoneGameIII(self, stoneValue: List[int]) -> str:

        @lru_cache(None)
        def dp(i, t):
            if i == len(stoneValue):
                return 0
            if t == 0:
                m = -math.inf
                s = 0
                for j in range(i, min(i + 3, len(stoneValue))):
                    s += stoneValue[j]
                    m = max(m, s + dp(j + 1, 1))
            else:
                m = math.inf
                s = 0
                for j in range(i, min(i + 3, len(stoneValue))):
                    s -= stoneValue[j]
                    m = min(m, s + dp(j + 1, 0))
            return m
        ans = dp(0, 0)
        if ans > 0:
            return 'Alice'
        elif ans < 0:
            return 'Bob'
        else:
            return 'Tie'
