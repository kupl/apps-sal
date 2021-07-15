class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        def dfs(remaining):
            nonlocal memo
            if remaining == 0:
                return 0
            if remaining < 0:
                return -1
            if memo[remaining]:
                return memo[remaining]
            
            # res initialize as infinity, but in this case
            # total amount is `amount`, we at most have `amount` 1 coins
            # so, `amount+1` can be considered as a maximum
            res = amount + 1
            for coin in coins:
                count = dfs(remaining - coin)
                if count == -1:
                    continue
                res = min(res, 1 + count)
            memo[remaining] = res if res != amount + 1 else -1
            return memo[remaining]
        memo = [None for _ in range(amount + 1)]
        return dfs(amount)
