class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles = collections.deque(sorted(piles)[::-1])
        s = 0
        while len(piles) > 0:
            piles.popleft()
            x = piles.popleft()
            piles.pop()
            s += x
        return s
