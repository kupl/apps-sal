class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        f = [float('inf') for i in range(amount + 1)]

        f[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                if i - coin >= 0 and f[i - coin] != float('inf'):
                    f[i] = min(f[i], f[i - coin] + 1)

        if f[-1] == float('inf'):
            return -1

        return f[-1]
