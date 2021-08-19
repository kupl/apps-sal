class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:

        def opt(v):
            if v == 0:
                return 0
            if v in memo:
                return memo[v]
            result = float('inf')
            for i in coins:
                if v - i >= 0:
                    result = min(result, opt(v - i) + 1)
                else:
                    continue
            memo[v] = result
            return memo[v]
        memo = {}
        coins = opt(amount)
        if coins == float('inf'):
            return -1
        else:
            return coins
