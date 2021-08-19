class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        piles = deque(piles)
        me = 0
        while piles:
            alice = piles.pop()
            if piles:
                me += piles.pop()
            if piles:
                bob = piles.popleft()
        return me
