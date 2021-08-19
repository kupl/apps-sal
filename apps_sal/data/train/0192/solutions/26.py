class Solution:
    def maxCoins(self, piles: List[int]) -> int:

        piles.sort()
        # piles = deque(piles)

        me = 0
        start, end = 0, len(piles) - 1
        # while len(piles) > 2:
        while start < end:
            # piles.pop()
            # me += piles.pop()
            # if piles:
            #     piles.popleft()
            if end - 1 > 0:
                me += piles[end - 1]
            start, end = start + 1, end - 2
        return me
