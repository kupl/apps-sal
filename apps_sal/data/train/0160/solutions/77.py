class Solution:
    from functools import lru_cache

    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)

        @lru_cache(None)
        def dp(i, j, asum, lsum, aturn):

            if i > j:
                return (0, 0)

            if aturn:
                asum += max(piles[i] + dp(i + 1, j, asum, lsum, False)[0], piles[j] + dp(i, j - 1, asum, lsum, False)[0])
            else:
                lsum += max(piles[i] + dp(i + 1, j, asum, lsum, True)[1], piles[j] + dp(i, j - 1, asum, lsum, True)[1])

            return (asum, lsum)

        asum, lsum = dp(0, n - 1, 0, 0, True)

        return bool(asum - lsum)
