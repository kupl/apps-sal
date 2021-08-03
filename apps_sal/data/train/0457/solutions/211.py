class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        s = list()
        import sys
        for i in range(0, amount + 1):
            s.append(sys.maxsize)
        s[0] = 0

        for i in range(1, amount + 1):
            m = sys.maxsize
            for j in range(0, len(coins)):
                if i - coins[j] >= 0:
                    m = min(m, s[i - coins[j]])
            if m == sys.maxsize:
                s[i] = m
            else:
                s[i] = m + 1
        if s[amount] == sys.maxsize:
            s[amount] = -1

        return s[amount]
