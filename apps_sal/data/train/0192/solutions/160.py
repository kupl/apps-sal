class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        sorted_coins = sorted(piles)
        print(sorted_coins)
        
        max_coins = 0
        
        while len(sorted_coins) > 0:
            sorted_coins.pop(0)
            sorted_coins.pop()
            max_coins += sorted_coins.pop()
            
        return max_coins
