class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dp(t):
            if t in d:
                return d[t]
            res = float('inf')
            for c in coins:
                if t - c >= 0:
                    res = min(res, dp(t - c) + 1)
            d[t] = res
            return res
        d = {0: 0}
        x = dp(amount)
        return x if x < float('inf') else -1
