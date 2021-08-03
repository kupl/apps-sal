class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        cache = {0: 0}

        def recurse(i):
            if i in cache:
                return cache[i]

            n = i + 1
            for coin in coins:
                curr = 0
                if i >= coin:
                    next_amount = recurse(i - coin)
                    if next_amount >= 0:
                        curr = 1 + next_amount
                if curr > 0:
                    n = min(n, curr)

            result = -1 if n == i + 1 else n
            cache[i] = result
            return result

        return recurse(amount)
