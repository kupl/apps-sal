class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        table = [0] + [amount + 1 for _ in range(amount)]
        for i in range(1, amount + 1):
            for coin in coins:
                if coin <= i:
                    sub_result = table[i - coin]
                    if sub_result + 1 < table[i]:
                        table[i] = sub_result + 1
        print(table)
        if table[amount] > amount:
            return -1
        else:
            return table[amount]
