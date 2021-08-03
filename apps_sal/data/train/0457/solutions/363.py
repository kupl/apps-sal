class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        coins.sort(reverse=True)
        d = {}
        for v in coins:
            d[v] = True
        min_coin = coins[-1]

        if not coins or not amount:
            return 0
        if len(coins) == 1:
            if amount % coins[0] == 0:
                return int(amount / coins[0])
            else:
                return -1

        self.memo = {}
        return self.fewest(coins, amount, d, min_coin)

    def fewest(self, coins, amount, d_value, min_coin):
        if amount in self.memo:
            return self.memo[amount]

        if amount in d_value:
            return 1
        elif amount < min_coin:
            return -1

        _min = float('inf')
        for v in coins:
            ret = self.fewest(coins, amount - v, d_value, min_coin)
            if ret > 0:
                _min = min(_min, ret + 1)

        _min = -1 if _min == float('inf') else _min
        self.memo[amount] = _min
        return _min
