class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount == 0:
            return 0

        s = list()
        s.append(0)

        for i in range(1, amount + 1):
            m = list()
            for j in range(0, len(coins)):
                if i - coins[j] >= 0:
                    m.append(s[i - coins[j]])
            mm = [item for item in m if item >= 0]
            if len(mm) == 0:
                s.append(-1)
            else:
                s.append(min(mm) + 1)

        return s[amount]
