class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 1:
            return 0

        self.coins = coins

        self.count = {}

        return self.helper(amount)

    def helper(self, rem):
        if rem < 0:
            return -1
        if rem == 0:
            return 0

        if (rem - 1) in self.count:
            return self.count[rem - 1]

        min_count = 1000000000
        for coin in self.coins:
            res = self.helper(rem - coin)
            if res >= 0 and res < min_count:
                min_count = res + 1

            if min_count == 1000000000:
                self.count[rem - 1] = -1
            else:
                self.count[rem - 1] = min_count

        return self.count[rem - 1]
