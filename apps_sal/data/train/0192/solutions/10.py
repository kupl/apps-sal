class Solution:

    def maxCoins(self, piles: List[int]) -> int:
        n = len(piles)
        piles = sorted(piles)
        piles = deque(piles)
        ans = 0
        while piles:
            piles.pop()
            ans += piles.pop()
            piles.popleft()
        return ans
