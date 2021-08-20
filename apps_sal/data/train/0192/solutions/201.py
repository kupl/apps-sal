class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        piles = deque(piles)
        me = 0
        while len(piles) > 2:
            piles.pop()
            me += piles.pop()
            if piles:
                piles.popleft()
        return me
