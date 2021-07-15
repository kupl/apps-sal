class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        if len(piles) == 3:
            return piles[1]
        print(len(piles)%2)
        print(list((i, a) for i, a in enumerate(sorted(piles)[len(piles)//3:]) if i % 2 == len(piles)%2))
        return sum(a for i, a in enumerate(sorted(piles)[len(piles)//3:]) if i % 2 == 0)
