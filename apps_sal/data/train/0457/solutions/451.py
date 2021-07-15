import math

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        self.c = set([x for x in coins if x<=amount])
        self.coins = list(self.c)
        self.dic = {}
        if amount == 0: return 0
        if amount in self.c: return 1
        res = math.inf
        for i in range(len(self.coins)):
            ci = self.dp(amount-self.coins[i])
            if ci >0:
                res = min(res, ci+1)
        return res if res != math.inf else -1

    def dp(self, amount):
        if amount in self.c:
            return 1
        if amount in self.dic:
            return self.dic[amount]
        list2 = [x for x in self.coins if x<=amount]
        if len(list2) == 0:
            return -1
        res = math.inf
        for i in range(len(list2)):
            ci = self.dp(amount-list2[i])
            if ci >0:
                res = min(res, ci+1)
        self.dic[amount] = res
        return res
