class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        @lru_cache(None)
        def dfs(amt, idx):
            if idx < 0:
                if amt == 0:
                    return 0
                else:
                    return float('inf')
            if amt < 0:
                return float('inf')
            if amt == coins[idx]:
                return 1
            return min(dfs(amt - coins[idx], idx) + 1, dfs(amt, idx - 1))
        res = dfs(amount, len(coins) - 1)
        return res if res < float('inf') else -1
