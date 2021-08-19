class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        count = {}
        for coin in coins:
            count[coin] = 1
        count[0] = 0
        for i in range(1, amount + 1):
            ans = amount + 1
            if i in list(count.keys()):
                continue
            for coin in coins:
                if i - coin > 0 and count[i - coin] != -1:
                    ans = min(count[i - coin], ans)
            if ans == amount + 1:
                count[i] = -1
            else:
                count[i] = ans + 1
        return count[amount]
