from functools import lru_cache


class Solution:

    @lru_cache(None)
    def recursive(self, i):
        if i >= self.n:
            return 0
        (ans, score) = (float('-inf'), 0)
        for k in range(3):
            if i + k < self.n:
                score += self.s[i + k]
                ans = max(ans, score - self.recursive(i + k + 1))
        return ans

    def stoneGameIII(self, stoneValue: List[int]) -> str:
        (self.n, self.s) = (len(stoneValue), stoneValue)
        self.recursive.cache_clear()
        x = self.recursive(0)
        return 'Alice' if x > 0 else 'Tie' if x == 0 else 'Bob'
