class Solution:

    def stoneGameIII(self, stoneValue: List[int]) -> str:

        @lru_cache(None)
        def dp(i, chance):
            n = len(stoneValue)
            if i >= len(stoneValue):
                return 0
            if not chance:
                ans = float('-inf')
                for j in range(i, i + 3):
                    if j < n:
                        ans = max(ans, dp(j + 1, 1) + sum(stoneValue[i:j + 1]))
            else:
                ans = float('inf')
                for j in range(i, i + 3):
                    if j < n:
                        ans = min(ans, dp(j + 1, 0) - sum(stoneValue[i:j + 1]))
            return ans
        score = dp(0, 0)
        if score > 0:
            return 'Alice'
        if score < 0:
            return 'Bob'
        return 'Tie'
