class Solution:
    def coinChange2(self, coins: List[int], amount: int, count) -> int:
        if amount < 0:
            return -1

        if amount == 0:
            return 0

        if(count[amount - 1] != 0):
            return count[amount - 1]

        min = 100000000000
        for i, c in enumerate(sorted(coins)[::-1]):
            ret = self.coinChange2(coins, amount - c, count)
            if(ret >= 0 and ret < min):
                min = 1 + ret
        if(min == 100000000000):
            count[amount - 1] = -1
        else:
            count[amount - 1] = min

        return count[amount - 1]

    def coinChange(self, coins: List[int], amount: int) -> int:
        if(amount < 1):
            return 0
        return self.coinChange2(coins, amount, [0] * amount)
