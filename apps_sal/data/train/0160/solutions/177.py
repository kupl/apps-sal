class Solution:
    # @lru_cache(None)
    def stoneGame(self, piles: List[int]) -> bool:
        result = dict()

        @lru_cache(None)
        def Alex(start, end) -> int:
            if start == end:
                return piles[start]
            # if (start, end) in result:
            #     return result[(start, end)]
            else:
                # result[(start, end)] = max(Lee(start + 1, end) + piles[start], Lee(start, end - 1) + piles[end])
                return max(Lee(start + 1, end) + piles[start], Lee(start, end - 1) + piles[end])
            # return result[(start, end)]

        def Lee(start, end) -> int:
            if start == end:
                return 0
            # if (start, end) in result:
            #     return result[(start, end)]
            else:
                # result[(start, end)] =  min(Alex(start + 1, end), Alex(start, end - 1))
                return min(Alex(start + 1, end), Alex(start, end - 1))
            # return result[(start, end)]
        Alex(0, len(piles) - 1)
        summ = sum(piles)
        # print(result[(0, len(piles - 1))])
        # print(summ)
        return Alex(0, len(piles) - 1) > (summ - Alex(0, len(piles) - 1))
