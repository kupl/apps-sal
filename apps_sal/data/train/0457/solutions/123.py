class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 0:
            return -1
        coins = sorted(coins)
        d = [amount + 1] * (amount + 1)
        d[0] = 0
        for i in range(amount + 1):
            for j in coins:
                if j <= i:
                    d[i] = min(d[i], d[i - j] + 1)
                else:
                    break
        if d[-1] > amount:
            return -1
        else:
            return d[-1]
