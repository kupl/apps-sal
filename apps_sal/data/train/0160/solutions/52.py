class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        '''
        def optimalMax(piles: List[int]):
            if len(piles)==1:
                return piles[0]
            return max(piles[0]+sum(piles[1:])-optimalMax(piles[1:]),
                   piles[-1]+sum(piles[:-1])-optimalMax(piles[:-1]))
        return optimalMax(piles)>sum(piles)/2
        '''
        def optimalMax(piles: List[int], dpTable, i, j, sum_):
            if j - i == 1:
                dpTable[i][j - 1] = piles[i]
                return piles[i]
            if dpTable[i][j - 1] <= 0:
                dpTable[i][j - 1] = max(sum_ - optimalMax(piles, dpTable, i + 1, j, sum_ - piles[i]),
                                        sum_ - optimalMax(piles, dpTable, i, j - 1, sum_ - piles[j - 1]))
            return dpTable[i][j - 1]
        dpTable = [[0 for _ in piles] for _ in piles]
        return optimalMax(piles, dpTable, 0, len(piles), sum(piles)) > sum(piles) / 2
