class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        list.sort(piles, reverse=True)
        print(piles)
        init = 0
        for j in range(len(piles) // 3):
            init = init + piles[j * 2 + 1]
        return init
