class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 1:
            return 0
        cnt = [0 for __ in range(amount)]
        return self.coinMake(coins, amount, cnt)

    def coinMake(self, coins, rem, count):
        if rem < 0:
            return -1
        if rem == 0:
            return 0
        if count[rem - 1] != 0:
            return count[rem - 1]
        MIN = 2**32 - 1
        for i in coins:
            res = self.coinMake(coins, rem - i, count)
            if res >= 0 and res < MIN:
                MIN = 1 + res
        count[rem - 1] = -1 if MIN == 2**32 - 1 else MIN
        return count[rem - 1]
