class Solution:
    def __init__(self):
        self.table = {}

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 0:
            return -1
        if amount == 0:
            return 0
        if amount in self.table:
            return self.table[amount]
        possible_answers = [self.coinChange(coins, amount - coin) + 1 for coin in coins]
        possible_answers = [ans for ans in possible_answers if ans >= 1]
        if possible_answers:
            ans = min(possible_answers)
        else:
            ans = -1
        self.table[amount] = ans
        return ans
