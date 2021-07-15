class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        l = [int(amount+1)] * int(amount+1)
        if amount == 0:
            return 0
        else:
            l[0] = 0
            for i in range(1, amount + 1):
                for coin in coins:
                    remainder = i - coin
                    if remainder < 0:
                        pass
                    else:
                        if l[i] > l[remainder] + 1:
                            l[i] = l[remainder] + 1
        if l[amount] == amount + 1:
            return -1
        else:
            return l[amount]

