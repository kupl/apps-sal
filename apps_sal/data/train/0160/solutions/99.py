class Solution:
    def stoneGame(self, piles: List[int]) -> bool:
        return self.dfs(piles, 0, len(piles) - 1, {})
        
    def dfs(self, piles, start, end, memo):
        if start > end:
            return 0
        elif start == end:
            return piles[start]
        elif (start, end) in memo:
            return memo[(start, end)]
        
        # choose one which is most optimal for the player
        L = piles[start] - self.dfs(piles, start + 1, end, memo)
        R = piles[end] - self.dfs(piles, start, end - 1, memo)
        memo[(start, end)] = max(L, R)
        return memo[(start, end)]
