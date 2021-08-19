class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0
        mem = [-1] * (amount + 1)
        mem[0] = 0
        for i in range(1, amount + 1):
            m = math.inf
            for c in coins:
                if i - c >= 0:
                    if mem[i - c] != -1 and mem[i - c] + 1 < m:
                        m = mem[i - c] + 1
            if m != math.inf:
                mem[i] = m
        print(mem)
        return mem[amount]
