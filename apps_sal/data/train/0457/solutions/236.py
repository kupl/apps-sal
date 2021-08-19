class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        mem = {}
        max_amount = 10 ** 4 + 1

        def cc(amount):
            mem[amount] = max_amount
            for coin in coins:
                dif = amount - coin
                if dif == 0:
                    mem[amount] = 1
                elif dif > 0:
                    if dif not in mem:
                        cc(dif)
                    mem[amount] = min(mem[amount], mem[dif] + 1)
        cc(amount)
        if mem[amount] == max_amount:
            return -1
        else:
            return mem[amount]
