class Solution:

    def __init__(self):
        self.count = []

    def coinChange(self, coins: List[int], amount: int) -> int:
        if len(self.count) < amount:
            self.count = [-1] * (amount + 1)
            self.skip = [False] * (amount + 1)
        if amount is 0:
            return 0
        elif amount < 0:
            return -1
        else:
            if self.count[amount] < 0 and (not self.skip[amount]):
                tmp = float('inf')
                for co in coins:
                    previous = self.coinChange(coins, amount - co)
                    if previous >= 0:
                        self.count[amount] = min(previous + 1, tmp)
                        tmp = self.count[amount]
                    else:
                        continue
                self.skip[amount] = True
            return self.count[amount]
