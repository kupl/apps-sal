class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort(reverse=True)
        (coins, turns, idx) = (0, 0, 1)
        while turns < len(piles) // 3:
            coins += piles[idx]
            idx += 2
            turns += 1
        return coins
