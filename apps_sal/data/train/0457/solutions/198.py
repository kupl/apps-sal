class Solution:
    def util(self, memo, coins, amount):
        if amount == 0:
            return 0
        if amount < 0:
            return -1
        minarr = []
        for coin in coins:
            if (amount - coin) not in memo:
                memo[(amount - coin)] = self.util(memo, coins, amount - coin)
            minarr.append(memo[(amount - coin)])

        minarr = [m for m in minarr if m != - 1]
        if not minarr:
            return -1
        return min(minarr) + 1

    def coinChange(self, coins: List[int], amount: int) -> int:
        memo = {}
        return self.util(memo, coins, amount)
