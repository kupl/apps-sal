class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 0 or not coins:
            return -1
        if amount == 0:
            return 0
        min_com = [0 for i in range(amount + 1)]
        for i in range(1, amount + 1):
            for c in coins:
                if i >= c and (min_com[i - c] > 0 or i - c == 0):
                    if min_com[i] == 0:
                        min_com[i] = min_com[i - c] + 1
                    else:
                        min_com[i] = min(min_com[i], min_com[i - c] + 1)
        if min_com[amount] == 0:
            return -1
        return min_com[amount]
