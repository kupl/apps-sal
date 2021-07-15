class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not coins or amount < 0:
            return -1

        f = [sys.maxsize for i in range(amount + 1)]

        f[0] = 0
        for i in range(1, len(f)):
            for coin in coins:
                if i - coin >= 0 and f[i - coin] != sys.maxsize:
                    f[i] = min(f[i], f[i - coin] + 1)

        if f[amount] == sys.maxsize:
            return -1

        return f[amount]
