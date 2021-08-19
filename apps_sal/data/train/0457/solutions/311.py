class Solution:

    def coinChange2(self, coins: List[int], amount: int) -> int:
        impossible = amount + 1
        cnts = [impossible] * impossible
        cnts[0] = 0
        for coin in coins:
            for x in range(coin, impossible):
                cnts[x] = min(cnts[x], cnts[x - coin] + 1)
        if cnts[amount] >= impossible:
            return -1
        return cnts[amount]

    def coinChange(self, coins: List[int], amount: int) -> int:
        impossible = amount + 1
        self.cnts = [0] * impossible

        def createCoins(total: int):
            if total == 0:
                return 0
            if self.cnts[total] != 0:
                return self.cnts[total]
            minCnt = impossible
            for coin in coins:
                if total - coin < 0:
                    continue
                cnt = createCoins(total - coin) + 1
                minCnt = min(cnt, minCnt)
            self.cnts[total] = minCnt
            return minCnt
        retV = createCoins(amount)
        if retV >= impossible:
            return -1
        return retV
