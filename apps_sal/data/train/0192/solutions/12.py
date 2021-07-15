class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles = sorted(piles, key=lambda x: -x)
        result = 0
        
        for i in range(len(piles) // 3):
            result += piles[1 + 2 * i]
        
        return result

