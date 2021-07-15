class Solution:
    from collections import deque
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        n = len(piles)//3
        return sum([piles[i] for i in range(n,n*3,2)])
            

