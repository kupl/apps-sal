class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        mem = {}
        mem[0] = 0

        def rec(amount):
            if amount < 0:
                return -1
            if amount in mem:
                return mem[amount]
            m = math.inf
            for c in coins:
                n = rec(amount - c)
                if n != -1 and n + 1 < m:
                    m = n + 1
            if m == math.inf:
                m = -1
            mem[amount] = m
            return m
        if amount == 0:
            return 0
        return rec(amount)
