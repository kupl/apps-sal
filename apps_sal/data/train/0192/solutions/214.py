class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        count = 0
        coinPiles = collections.deque(sorted(piles))
        while len(coinPiles) > 0:
            coinPiles.pop()
            count += coinPiles.pop()
            coinPiles.popleft()
        return count
