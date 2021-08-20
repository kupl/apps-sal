class Solution:

    def coinChange(self, coins: List[int], amount: int) -> int:
        l = [amount + 1] * (amount + 1)
        for i in range(len(l)):
            if i == 0:
                l[i] = 0
            elif all((i < c for c in coins)):
                l[i] = -1
            else:
                for j in range(len(coins)):
                    if i >= coins[j]:
                        num = i - coins[j]
                        if num > 0 and l[num] == -1:
                            if l[i] != amount + 1:
                                continue
                            else:
                                l[i] = -1
                        else:
                            comb = l[num] + 1
                            if l[i] == -1:
                                l[i] = amount + 1
                            if l[i] >= comb:
                                l[i] = comb
        return l[-1]
