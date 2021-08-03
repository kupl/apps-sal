class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        value = [-1] * (amount + 1)
        value[0] = 0

        for j in range(amount + 1):
            for i in range(len(coins)):
                if j > coins[i]:
                    if value[j - coins[i]] != -1:
                        if value[j] == -1:
                            value[j] = value[j - coins[i]] + 1
                        else:
                            value[j] = min(value[j], value[j - coins[i]] + 1)
                if j == coins[i]:
                    value[j] = 1
        print(value)
        return value[-1]
