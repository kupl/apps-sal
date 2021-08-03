class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if amount < 1:
            return 0
        cnt = [0 for __ in range(amount)]
        return self.coinMake(coins, amount, cnt)

    def coinMake(self, coins, rem, count):
        if rem < 0:
            return -1
        if rem == 0:
            return 0
        if count[rem - 1] != 0:
            return count[rem - 1]
        MIN = 2**32 - 1
        for i in coins:
            res = self.coinMake(coins, rem - i, count)
            if res >= 0 and res < MIN:
                MIN = 1 + res
        count[rem - 1] = -1 if MIN == 2**32 - 1 else MIN
        return count[rem - 1]

        #recursive + memo
        #memo = [2**32 - 1 for __ in range(amount + 1)]
        #memo[0] = 0
        # return self.coinChangeDFS(coins, amount, memo)

    # def coinChangeDFS(self, coins, target, memo):
    #    if target < 0: return -1
    #    if memo[target] != 2**32 -1: return memo[target]
    #    for i in range(len(coins)):
    #        tmp = self.coinChangeDFS(coins, target - coins[i], memo)
    #        if tmp >= 0: memo[target] = min(memo[target], tmp + 1)
    #    return -1 if memo[target] == 2**32 - 1 else memo[target]

        # iterative
        #DP = [amount + 1 for __ in range(amount + 1)]
        #DP[0] = 0

        # for i in range(amount + 1):
        #    for j in range(len(coins)):
        #        if coins[j] <= i:
        #            DP[i] = min(DP[i], DP[i - coins[j]] + 1)
        # return -1 if DP[amount] > amount else DP[amount]
