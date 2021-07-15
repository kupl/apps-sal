class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        def dp(m):
            if m in coins: return 1
            if m == 0: return 0
            if m < 0: return float('inf')
            
            if m not in memo:
                ans = float('inf')
                for v in coins:
                    ans = min(1 + dp(m - v), ans)
                memo[m] = ans
            return memo[m]
        return dp(amount) if dp(amount)!= float('inf') else -1

