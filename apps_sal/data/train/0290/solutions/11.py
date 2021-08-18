import functools


class Solution:

    @functools.lru_cache(None)
    def dp(self, i, j):
        if j - i < 2:
            return 0
        options = [j - i + self.dp(i, k) + self.dp(k, j) for k in self.cuts if i < k and k < j]
        if len(options) == 0:
            return 0
        result = min(options)
        return result

    def minCost(self, n: int, cuts) -> int:
        self.cuts = cuts
        return self.dp(0, n)
