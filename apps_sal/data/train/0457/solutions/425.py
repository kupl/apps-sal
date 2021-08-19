class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        dic = {0: 0}

        def change(amount):
            if amount < 0:
                return -1
            if amount in dic:
                return dic[amount]
            res = [change(amount - i) for i in coins if change(amount - i) >= 0]
            if not res:
                dic[amount] = -1
            else:
                dic[amount] = min(res) + 1
            return dic[amount]
        return change(amount)
