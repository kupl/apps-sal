class Solution:

    def stoneGame(self, piles: List[int]) -> bool:
        result = dict()

        @lru_cache(None)
        def Alex(start, end) -> int:
            if start == end:
                return piles[start]
            else:
                return max(Lee(start + 1, end) + piles[start], Lee(start, end - 1) + piles[end])

        def Lee(start, end) -> int:
            if start == end:
                return 0
            else:
                return min(Alex(start + 1, end), Alex(start, end - 1))
        Alex(0, len(piles) - 1)
        summ = sum(piles)
        return Alex(0, len(piles) - 1) > summ - Alex(0, len(piles) - 1)
