class Solution:
    def helper(self, coins, amount, cache, current=[]):
        if amount == 0:
            return 0
        if amount < 0:
            return -1

        else:
            if amount in cache:
                return cache[amount]

            currMin = sys.maxsize

            for coin in coins:
                current.append(coin)  # choose that coin
                currNum = self.helper(coins, amount - coin, cache, current)

                if currNum != -1:
                    if currNum < currMin:
                        currMin = currNum + 1

                current.pop()

            cache[amount] = currMin
            return currMin

    def coinChange(self, coins, amount):
        cache = {}
        val = self.helper(coins, amount, cache)

        # if val == sys.maxsize:
        #     return -1
        # else:
        #     return val

        # for each slot in memoization array, subtract each coin from it
        # find min and add 1

        # F(0) is 0
        memo = [sys.maxsize] * (amount + 1)
        memo[0] = 0

        for i in range(1, amount + 1):
            for coin in coins:
                newIndex = i - coin

                if newIndex >= 0:
                    if memo[newIndex] + 1 < memo[i]:
                        memo[i] = memo[newIndex] + 1

        if memo[amount] == sys.maxsize:
            return -1
        else:
            return memo[amount]
