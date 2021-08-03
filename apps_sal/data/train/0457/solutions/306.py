class Solution:

    def helper(self, coins, amount, total, count, mem):

        if total > amount:
            return

        if total == amount:
            if total not in mem:
                mem[total] = count
            else:
                mem[total] = min(mem[total], count)
            return

        for c in coins:
            if total + c not in mem or mem[total + c] > count + 1:
                mem[total + c] = count + 1
                self.helper(coins, amount, total + c, count + 1, mem)

        return

    def coinChange(self, coins: List[int], amount: int) -> int:

        if not amount:
            return 0

        if amount < min(coins):
            return -1

        mem = {}
        coins.sort(reverse=True)
        self.helper(coins, amount, 0, 0, mem)

        if amount in mem:
            return mem[amount]
        else:
            return -1
