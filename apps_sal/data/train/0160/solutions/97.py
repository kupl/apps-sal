class Solution:

    def stoneGame(self, piles: List[int]) -> bool:
        n = len(piles)
        self.memo = [[float('-inf') for _ in range(n)] for _ in range(n)]
        return self.dfs(piles, 0, n - 1) > 0

    def dfs(self, piles, left, right):
        if left == right:
            return piles[left]
        if self.memo[left][right] == float('-inf'):
            self.memo[left][right] = max(piles[left] - self.dfs(piles, left + 1, right), piles[right] - self.dfs(piles, left, right - 1))
        return self.memo[left][right]
